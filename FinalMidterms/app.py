from flask import Flask, render_template, jsonify, request
from Agents import *
from Problems import *
import json

app = Flask(__name__)

result = None
main_obj = None
started = False
Finished = True

@app.route('/')
def home():
    return render_template('main.html') #for home html

@app.route('/nqueens')
def nqueensenv():
    return render_template('nqueensenv.html')

@app.route('/nqueens/start',methods=['POST'])
def nqueensenvstart():
    if started == False:
        data = json.loads(request.data.decode('utf-8'))
        n = int(data['n'])
        algorithm = data['algorithm']

        if algorithm == 'bfs':
            X = NQueenBFSAgent(n)
            result = X.run()
        elif algorithm == 'dfs':
            X = NQueenDFSAgent(n)
            result = X.run()
        elif algorithm == 'dls':
            X = NQueenDLSAgent(n)
            result = X.run()
        elif algorithm == 'ids':
            X = NQueenIDSAgent(n)
            result = X.run()
        elif algorithm == 'greedy':
            X = NQueenGreedyAgent(n)
            result = X.run()
        elif algorithm == 'astar':
            X = NQueenAStarAgent(n)
            result = X.run()
        elif algorithm == 'ucs':
            X = NQueenUCSAgent(n)
            result = X.run()
        elif algorithm == 'hillclimbing':
            X = NQueenHillClimbingAgent(n)
            result = X.run()
            result = list(result)[0]
        elif algorithm == 'rrhillclimbing':
            X = NQueenRRHillClimbingAgent(n,steps=10)
            result = X.run()
            result = list(result)[0]
        elif algorithm == 'genetic':
            X = NQueenGeneticAlgorithmAgent(n,population=100,steps=10,mutation_prob=.2)
            result = X.run()
        elif algorithm == 'simulatedannealing':
            X = NQueenSimulatedAnnealingAgent(n=n,T=1000,coefficient=.99,threshold=1)
            result, value = X.run()
        elif algorithm == 'localbeamsearch':
            X = NQueenLocalBeamAgent(n=n,k=10)
            result, value = X.run()
        
        print('xxxxxxxxxxxxxxxxxxxx',result)
        return jsonify({
            'goal' : result
        })

@app.route('/nqueens/result')
def nqueensenvresult():
    if result != None:
        return jsonify(result)

# Map Coloring

@app.route('/maps')
def maps():
    return render_template('maps.html')

@app.route('/map/<name>')
def mapenv(name):
    temp = ''.join([name,'map.html'])
    return render_template(temp)

@app.route('/map/start',methods=['POST'])
def mapstart():
    data = json.loads(request.data.decode('utf-8'))
    forward_checking = data['forward_checking']
    arc_consistency = data['arc_consistency']
    mrv = data['mrv']
    degree = data['degree']
    lcv = data['lcv']
    map_name = data['map_name']
    color_count = data['color_count']

    global main_obj
    X = MapColoringCSPAgent(map_name=map_name,color_count=int(color_count),forward_checking=forward_checking,arc_consistency=arc_consistency,mrv_heuristic=mrv,degree_heuristic=degree,lcv_heuristic=lcv)
    main_obj = X
    res = X.run()

@app.route('/map/stop')
def mapstop():
    global main_obj
    main_obj.stop = True
    

@app.route('/map/getmap')
def getmap():
    main_obj.pause = True
    try:
        temp = main_obj.current_element.assignments
        done = main_obj.done
        have_answer = main_obj.have_answer
        main_obj.pause = False

        return jsonify({
            'map' : temp,
            'done' : done,
            'have_answer' : have_answer
        })
    except:
        main_obj.pause = False

app.debug = False
app.run(threaded=True)