import streamlit as st
import math


nodes = ("Lisboa", "Madrid", "Barcelona", "Paris" , "Zurique" , "Luxembourg", "Berlin")

time_car = {
    'Lisboa': {'Madrid': 353, 'Barcelona': 691,'Paris': 1000,'Zurique': 1253,'Luxembourg': 1223,'Berlin': 1620},
    'Madrid': {'Lisboa': 353, 'Barcelona': 377,'Paris': 774,'Zurique': 955,'Luxembourg': 990,'Berlin': 1416},
    'Barcelona': {'Lisboa': 691, 'Madrid': 377,'Paris': 374,'Zurique': 618,'Luxembourg': 680,'Berlin': 1107},
    'Paris': {'Lisboa': 100, 'Madrid': 774,'Barcelona': 374,'Zurique': 426,'Luxembourg': 245,'Berlin': 663},
    'Zurique': {'Lisboa': 1253, 'Madrid': 955,'Barcelona': 618,'Paris': 426,'Luxembourg': 311,'Berlin': 546},
    'Luxembourg': {'Lisboa': 1223, 'Madrid': 990,'Barcelona': 680,'Paris': 245,'Zurique': 311,'Berlin': 503},
	'Berlin': {'Lisboa': 1620, 'Madrid': 1416,'Barcelona': 1107,'Paris': 663,'Zurique': 546,'Luxembourg': 503}
}

price_car = {
    'Lisboa': {'Madrid': 90.1, 'Barcelona': 160.3,'Paris': 305.1,'Zurique': 404.3,'Luxembourg': 303.8,'Berlin': 440.6},
    'Madrid': {'Lisboa': 90.1, 'Barcelona': 70.2,'Paris': 244.6,'Zurique': 299.6,'Luxembourg': 323.4,'Berlin': 380.2},
    'Barcelona': {'Lisboa': 160.3, 'Madrid': 70.2,'Paris': 190,'Zurique': 235.8,'Luxembourg': 221.6,'Berlin': 302.2},
    'Paris': {'Lisboa': 305.1, 'Madrid': 244.6,'Barcelona': 190,'Zurique': 137.7,'Luxembourg': 87.4,'Berlin': 136.4},
    'Zurique': {'Lisboa': 404.3, 'Madrid': 299.6,'Barcelona': 235.8,'Paris': 137.7,'Luxembourg': 101.5,'Berlin': 139.3},
    'Luxembourg': {'Lisboa': 303.8, 'Madrid': 323.4,'Barcelona': 221.6,'Paris': 87.4,'Zurique': 101.5,'Berlin': 87.3},
	'Berlin': {'Lisboa': 303.8, 'Madrid': 323.4,'Barcelona': 221.6,'Paris': 87.4,'Zurique': 101.5,'Luxembourg': 87.3}
}

time_train = {
    'Lisboa': {'Madrid': 521, 'Barcelona': 699, 'Paris': 1134, 'Zurique': 1560, 'Luxembourg': 1447, 'Berlin': 1845},
    'Madrid': {'Lisboa': 521, 'Barcelona': 165, 'Paris': 420, 'Zurique': 986, 'Luxembourg': 927, 'Berlin': 1226},
    'Barcelona': {'Lisboa': 699, 'Madrid': 165, 'Paris': 405, 'Zurique': 871, 'Luxembourg': 909, 'Berlin': 1205},
    'Paris': {'Lisboa': 1134, 'Madrid': 420, 'Barcelona': 405, 'Zurique': 245, 'Luxembourg': 135, 'Berlin': 490},
    'Zurique': {'Lisboa': 1560, 'Madrid': 986, 'Barcelona': 871, 'Paris': 245, 'Luxembourg': 483, 'Berlin': 480},
    'Luxembourg': {'Lisboa': 1447, 'Madrid': 927, 'Barcelona': 909, 'Paris': 135, 'Zurique': 483, 'Berlin': 704},
    'Berlin': {'Lisboa': 1845, 'Madrid': 1226, 'Barcelona': 1205, 'Paris': 490, 'Zurique': 480, 'Luxembourg': 704}
}

price_train = {
    'Lisboa': {'Madrid': 75, 'Barcelona': 145, 'Paris': 150, 'Zurique': 160, 'Luxembourg': 180, 'Berlin': 210},
    'Madrid': {'Lisboa': 75, 'Barcelona': 50, 'Paris': 130, 'Zurique': 250, 'Luxembourg': 240, 'Berlin': 220},
    'Barcelona': {'Lisboa': 145, 'Madrid': 50, 'Paris': 95, 'Zurique': 180, 'Luxembourg': 170, 'Berlin': 190},
    'Paris': {'Lisboa': 150, 'Madrid': 130, 'Barcelona': 95, 'Zurique': 90, 'Luxembourg': 50, 'Berlin': 85},
    'Zurique': {'Lisboa': 160, 'Madrid': 250, 'Barcelona': 180, 'Paris': 90, 'Luxembourg': 65, 'Berlin': 70},
    'Luxembourg': {'Lisboa': 180, 'Madrid': 240, 'Barcelona': 170, 'Paris': 50, 'Zurique': 65, 'Berlin': 75},
    'Berlin': {'Lisboa': 210, 'Madrid': 220, 'Barcelona': 190, 'Paris': 85, 'Zurique': 70, 'Luxembourg': 75}
}

time_plane = { 
    'Lisboa': {'Madrid': 90, 'Barcelona': 110,'Paris': 145,'Zurique': 270,'Luxembourg': 165,'Berlin': 210},
    'Madrid': {'Lisboa': 90, 'Barcelona': 85,'Paris': 125,'Zurique': 140,'Luxembourg': 140,'Berlin': 180},
    'Barcelona': {'Lisboa': 110, 'Madrid': 85,'Paris': 120,'Zurique': 110,'Luxembourg': 125,'Berlin': 160},
    'Paris': {'Lisboa': 145, 'Madrid': 125,'Barcelona': 120,'Zurique': 75,'Luxembourg': 60,'Berlin': 205},
    'Zurique': {'Lisboa': 270, 'Madrid': 140,'Barcelona': 110,'Paris': 75,'Luxembourg': 55,'Berlin': 90},
    'Luxembourg': {'Lisboa': 165, 'Madrid': 140,'Barcelona': 125,'Paris': 60,'Zurique': 55,'Berlin': 90},
	'Berlin': {'Lisboa': 210, 'Madrid': 180,'Barcelona': 160,'Paris': 205,'Zurique': 90,'Luxembourg': 90}
    }

price_plane = { 
    'Lisboa': {'Madrid': 130, 'Barcelona': 120,'Paris': 208,'Zurique': 221,'Luxembourg': 246,'Berlin': 351},
    'Madrid': {'Lisboa': 130, 'Barcelona': 199,'Paris': 188,'Zurique': 274,'Luxembourg': 259,'Berlin': 252},
    'Barcelona': {'Lisboa': 120, 'Madrid': 199,'Paris': 98,'Zurique': 140,'Luxembourg': 134,'Berlin': 178},
    'Paris': {'Lisboa': 208, 'Madrid': 188,'Barcelona': 98,'Zurique': 204,'Luxembourg': 208,'Berlin': 210},
    'Zurique': {'Lisboa': 221, 'Madrid': 274,'Barcelona': 140,'Paris': 204,'Luxembourg': 254,'Berlin': 157},
    'Luxembourg': {'Lisboa': 246, 'Madrid': 259,'Barcelona': 134,'Paris': 208,'Zurique': 254,'Berlin': 251},
	'Berlin': {'Lisboa': 351, 'Madrid': 252,'Barcelona': 178,'Paris': 210,'Zurique': 157,'Luxembourg': 251}
    }

table_routes = {}

table_routes['time_car'] = time_car
table_routes['price_car'] = price_car
table_routes['time_train'] = time_train
table_routes['price_train'] = price_train
table_routes['time_plane'] = time_plane
table_routes['price_plane'] = price_plane


def find_route(current, end, otimize, travel_type):

    array_check = table_routes[otimize + '_' + travel_type]

    unvisited = {node: float('inf') for node in nodes}
    current_value = 0
    unvisited[current] = current_value
    visited, parents = {}, {}
    
    while unvisited:
        min_vertex = min(unvisited, key=unvisited.get)
        for neighbour, distance in array_check[current].items():
            if neighbour not in unvisited:
                continue
            new_distance = current_value + distance
            if unvisited[neighbour] == float('inf') or unvisited[neighbour] > new_distance:
                unvisited[neighbour] = new_distance
                parents[neighbour] = min_vertex
        visited[current] = current_value
        unvisited.pop(min_vertex)
        if min_vertex == end:
            break
        candidates = [node for node in unvisited.items() if node[1]]
        current, current_value = min(candidates, key=lambda x: x[1])
    
    return parents, current_value

def generate_path(parents, start , end):
	path=[end]
	while True:
		key=parents[path[0]]
		path.insert (0, key)
		if key == start:
			break
	return " ---> ".join(path)

def cost_benefit(time, price, time_1, price_1, time_2, price_2):

    valor_base = time/price

    valor=(time_1-time_2)/(price_1-price_2)

    if valor < valor_base:
        return 1
    else:
        return 2
    

st.title("Roteiro Europa: Melhor Transporte")

st.html("<a href='https://aeeddipiaget.pt/grafo/' target='_blank'>Grafo</a>")

col1, col2 = st.columns(2)
with col1:
    origem = st.selectbox("Origem", nodes)
with col2:
    destino = st.selectbox("Destino", nodes)

criterio = st.radio("Critério de otimização", ["time", "price", "time_price"], format_func=lambda x: "Tempo" if x == "time" else "Preço" if x == "price" else "Tempo e Preço")

time, price = 0,0
if criterio == "time_price":
    col1, col2 = st.columns(2)
    with col1:
        time = st.text_input("Tempo(minutos)")
    with col2:
        price = st.text_input("Preço(euros)")

if origem == destino:
    st.warning("A origem e o destino não podem ser iguais.")
elif time == "" or price == "":
    st.warning("Tem de colocar valores da relação tempo preço.")
else:
    if st.button("Calcular melhor transporte"):
        if criterio == "time_price":
            parents_time,time_car = find_route(origem, destino, "time", "car")
            parents_time,time_train = find_route(origem, destino, "time", "train")
            parents_time,time_plane = find_route(origem, destino, "time", "plane")

            parents_price,price_car = find_route(origem, destino, "price", "car")
            parents_price,price_train = find_route(origem, destino, "price", "train")
            parents_price,price_plane = find_route(origem, destino, "price", "plane")

            value_cost = cost_benefit(int(time), int(price), time_car, price_car, time_train, price_train)
            if value_cost == 1:
                value_cost = cost_benefit(int(time), int(price),time_car, price_car, time_plane, price_plane)
                if value_cost == 1:
                    meio = "Carro"
                else:
                    meio = "Avião"
            else:
                value_cost = cost_benefit(int(time), int(price),time_train, price_train, time_plane, price_plane)
                if value_cost == 1:
                    meio = "Comboio"
                else:
                    meio = "Avião"

            if meio == "Carro":
                value_time = time_car
                value_price = price_car
                parents,time_car = find_route(origem, destino, "time", "car")
                parents_price,price_car = find_route(origem, destino, "price", "car")
            if meio == "Comboio":
                value_time = time_train
                value_price = price_train
                parents_time,time_train = find_route(origem, destino, "time", "train")
                parents_price,price_train = find_route(origem, destino, "price", "train")
            if meio == "Avião":
                value_time = time_plane
                value_price = price_plane
                parents_time,time_train = find_route(origem, destino, "time", "train")
                parents_price,price_plane = find_route(origem, destino, "price", "plane")

            path_time = generate_path(parents_time, origem, destino)
            path_price = generate_path(parents_price, origem, destino)
            
            st.success(f"Melhor meio de transporte: **{meio}**\n\nTempo: {path_time}\n\nPreço: {path_price}\n\n{criterio.replace('_', ' + ').title()}: **{value_time // 60} horas e {value_time % 60} minutos ou {value_price:.2f} euros**")

        else:
            parents,car = find_route(origem, destino, criterio, "car")
            parents,train = find_route(origem, destino, criterio, "train")
            parents,plane = find_route(origem, destino, criterio, "plane")
            if(car < train and car < plane):
                meio = "Carro"
                valor = car
            if(train < car and train < plane):
                meio = "Comboio"
                valor = train
            if(plane < car and plane < train):
                meio = "Avião"
                valor = plane
            unidade = f"{valor // 60} horas e {valor % 60} minutos" if criterio == "time" else f"{valor:.2f} euros"
            path = generate_path(parents, origem, destino)
            st.success(f"Melhor meio de transporte: **{meio}**\n\n{path}\n\n{criterio.capitalize()}: **{unidade}**")

        st.html("<p>Verificar com dados reais:<a href='' target='_blank'>Carro</a> <a href='' target='_blank'>Comboio</a> <a href='' target='_blank'>Avião</a></p>")
