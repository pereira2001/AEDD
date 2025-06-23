import streamlit as st


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

# time_train = { 
#     'Lisboa': {'Madrid': , 'Barcelona': ,'Paris': ,'Zurique': ,'Luxembourg': ,'Berlin': },
#     'Madrid': {'Lisboa': , 'Barcelona': ,'Paris': ,'Zurique': ,'Luxembourg': ,'Berlin': },
#     'Barcelona': {'Lisboa': , 'Madrid': ,'Paris': ,'Zurique': ,'Luxembourg': ,'Berlin': },
#     'Paris': {'Lisboa': , 'Madrid': ,'Barcelona': ,'Zurique': ,'Luxembourg': ,'Berlin': },
#     'Zurique': {'Lisboa': , 'Madrid': ,'Barcelona': ,'Paris': ,'Luxembourg': ,'Berlin': },
#     'Luxembourg': {'Lisboa': , 'Madrid': ,'Barcelona': ,'Paris': ,'Zurique': ,'Berlin': },
# 	'Berlin': {'Lisboa': , 'Madrid': ,'Barcelona': ,'Paris': ,'Zurique': ,'Luxembourg': }
#     }

# price_train = { 
#     'Lisboa': {'Madrid': , 'Barcelona': ,'Paris': ,'Zurique': ,'Luxembourg': ,'Berlin': },
#     'Madrid': {'Lisboa': , 'Barcelona': ,'Paris': ,'Zurique': ,'Luxembourg': ,'Berlin': },
#     'Barcelona': {'Lisboa': , 'Madrid': ,'Paris': ,'Zurique': ,'Luxembourg': ,'Berlin': },
#     'Paris': {'Lisboa': , 'Madrid': ,'Barcelona': ,'Zurique': ,'Luxembourg': ,'Berlin': },
#     'Zurique': {'Lisboa': , 'Madrid': ,'Barcelona': ,'Paris': ,'Luxembourg': ,'Berlin': },
#     'Luxembourg': {'Lisboa': , 'Madrid': ,'Barcelona': ,'Paris': ,'Zurique': ,'Berlin': },
# 	'Berlin': {'Lisboa': , 'Madrid': ,'Barcelona': ,'Paris': ,'Zurique': ,'Luxembourg': }
#     }

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


def find_route(current, end, otimize):
    current_first = current
    
    array_check_car = {}
    array_check_train = {}
    array_check_plane = {}

    match otimize:
        case 'time':
            array_check_car = time_car
            # array_check_train = time_train
            array_check_plane = time_plane
        case 'price':
            array_check_car = price_car
            # array_check_train = price_train
            array_check_plane = price_plane
        case _:
            print("Erro")
            return
    

    #Carro
    unvisited = {node: float('inf') for node in nodes}
    current_value_car = 0
    unvisited[current] = current_value_car
    visited, parents = {}, {}
    while unvisited: 
        min_vertex = min(unvisited, key=unvisited.get)
        for neighbour, distance in array_check_car[current].items():
            if neighbour not in unvisited:
                continue
            new_distance = current_value_car + distance
            if unvisited[neighbour] == float('inf'):
                unvisited[neighbour] = new_distance
                parents[neighbour] = min_vertex
        visited[current] = current_value_car
        unvisited.pop(min_vertex)
        if min_vertex == end:
            break
        candidates = [node for node in unvisited.items() if node[1]]
        # print(f"{candidates = }")
        current, current_value_car = min(candidates, key=lambda x: x[1])
        
    
    # #Train
    current = current_first
    # unvisited = {node: float('inf') for node in nodes}
    current_value_train = 1000000
    # unvisited[current] = current_value_train
    # visited, parents = {}, {}
    # while unvisited:
    #     min_vertex = min(unvisited, key=unvisited.get)
    #     for neighbour, distance in array_check_train[current].items():
    #         if neighbour not in unvisited:
    #             continue
    #         new_distance = current_value_train + distance
    #         if unvisited[neighbour] == float('inf'):
    #             unvisited[neighbour] = new_distance
    #             parents[neighbour] = min_vertex
    #     visited[current] = current_value_train
    #     unvisited.pop(min_vertex)
    #     if min_vertex == end:
    #         break
    #     candidates = [node for node in unvisited.items() if node[1]]
    #     current, current_value_train = min(candidates, key=lambda x: x[1])

    #Plane
    current = current_first
    unvisited = {node: float('inf') for node in nodes}
    current_value_plane = 0
    unvisited[current] = current_value_plane
    visited, parents = {}, {}
    while unvisited:
        min_vertex = min(unvisited, key=unvisited.get)
        for neighbour, distance in array_check_plane[current].items():
            if neighbour not in unvisited:
                continue
            new_distance = current_value_plane + distance
            if unvisited[neighbour] == float('inf'):
                unvisited[neighbour] = new_distance
                parents[neighbour] = min_vertex
        visited[current] = current_value_plane
        unvisited.pop(min_vertex)
        if min_vertex == end:
            break
        candidates = [node for node in unvisited.items() if node[1]]
        current, current_value_plane = min(candidates, key=lambda x: x[1])

    print(f"{current_value_car:.2f}")
    print(f"{current_value_train:.2f}")
    print(f"{current_value_plane:.2f}")
    
    if(current_value_car < current_value_train and current_value_car < current_value_plane):
        return "Car", current_value_car
    if(current_value_train < current_value_car and current_value_train < current_value_plane):
        return "Train", current_value_train
    if(current_value_plane < current_value_car and current_value_plane < current_value_train):
        return "Plane", current_value_plane

    
# Interface Streamlit
st.title("Roteiro Europa: Melhor Transporte")

col1, col2 = st.columns(2)
with col1:
    origem = st.selectbox("Origem", nodes)
with col2:
    destino = st.selectbox("Destino", nodes)

criterio = st.radio("Critério de otimização", ["time", "price"], format_func=lambda x: "Tempo" if x == "time" else "Preço")

if origem == destino:
    st.warning("A origem e o destino não podem ser iguais.")
else:
    if st.button("Calcular melhor transporte"):
        meio, valor = find_route(origem, destino, criterio)
        unidade = "minutos" if criterio == "time" else "euros"
        st.success(f"Melhor meio de transporte: **{meio}**\n\n{criterio.capitalize()}: **{valor:.2f} {unidade}**")
