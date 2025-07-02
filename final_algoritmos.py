import streamlit as st
import pandas as pd

#Cidades
nodes = ("Lisboa", "Madrid", "Barcelona", "Paris" , "Zurique" , "Luxembourg", "Berlin")

#Lat, Long Cidades
nodes_lat_long = {
    'Lisboa': (38.7223, -9.1393),
    'Madrid': (40.4168, -3.7038),
    'Barcelona': (41.3851, 2.1734),
    'Paris': (48.8566, 2.3522),
    'Zurique': (47.3769, 8.5417),
    'Luxembourg': (49.6116, 6.1319),
    'Berlin': (52.5200, 13.4050)
}


#Grafos de Tempo e Preço Carro
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

#Grafos de Tempo e Preço Comboio
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

#Grafos de Tempo e Preço Avião
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

#Tabela de rotas
table_routes = {}

table_routes['time_car'] = time_car
table_routes['price_car'] = price_car
table_routes['time_train'] = time_train
table_routes['price_train'] = price_train
table_routes['time_plane'] = time_plane
table_routes['price_plane'] = price_plane

def df_order(data):
    """
        Função para ordenar a tabela com Lisboa no inicio
        data -> valores da tabela

        Retorna:
        df -> tabela ordenada
    """
    
    df = pd.DataFrame(data).T
    
    #Coloca linhas por ordem alfabetica
    rows = sorted(df.index.tolist())
    
    #Coloca Lisboa primeiro em colunas
    cols = sorted(df.columns.tolist())

    df = df.loc[rows, cols]
    return df

def show_table(title, data):
    """
        Função para escrever o titulo e tabela no programa
        title -> titulo da tabela
        data -> valores da tabela
    """
    st.header(title)
    df = df_order(data)
    st.dataframe(df)

def find_route(current, end, otimize, travel_type):
    """
        Função que encontra a rota mais curta entre dois pontos, utilizando o algoritmo de Dijkstra.
        current -> ponto de partida
        end -> ponto de chegada
        otimize -> otimização da rota (time ou price)
        travel_type -> tipo de veiculo (car, train, plane)

        Retorna:
        parents -> dicionário com a rota mais curta
        current_value -> valor do tempo ou preço da rota mais curta
    """

    # Criação do array de nós
    array_check = table_routes[otimize + '_' + travel_type]

    # Criação do array de nós visitados, por visitar e variaveis auxiliares
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

def find_route_both(current, end, otimize_1, otimize_2, travel_type):
    """
        Função que encontra a rota mais curta entre dois pontos, utilizando o algoritmo de Dijkstra.
        current -> ponto de partida
        end -> ponto de chegada
        otimize_1 -> otimização da rota principal (time ou price)
        otimize_2 -> otimização da rota auxiliar (time ou price)
        travel_type -> tipo de veiculo (car, train, plane)

        Retorna:
        parents -> dicionário com a rota mais curta
        current_value -> valor do otimize_1 da rota mais curta
        current_value -> valor do otimize_2 da rota mais curta

    """
    array_check = table_routes[otimize_1 + '_' + travel_type]
    array_check_aux = table_routes[otimize_2 + '_' + travel_type]

    unvisited = {node: float('inf') for node in nodes}
    unvisited_aux = {node: float('inf') for node in nodes}
    current_value = 0
    current_value_aux = 0
    unvisited[current] = current_value
    visited, parents = {}, {}
    unvisited_aux[current] = current_value_aux
    
    while unvisited:
        min_vertex = min(unvisited, key=unvisited.get)
        for neighbour, distance in array_check[current].items():
            if neighbour == "Zurique":
                print(neighbour)
            if neighbour not in unvisited:
                continue
            distance_aux = array_check_aux[current][neighbour]
            new_distance = current_value + distance
            new_distance_aux = current_value_aux + distance_aux
            if unvisited[neighbour] == float('inf') or unvisited[neighbour] > new_distance:
                unvisited[neighbour] = new_distance
                unvisited_aux[neighbour] = new_distance_aux
                parents[neighbour] = min_vertex
        visited[current] = current_value
        unvisited.pop(min_vertex)
        unvisited_aux.pop(min_vertex)
        if min_vertex == end:
            break
        candidates = [node for node in unvisited.items() if node[1]]
        # candidates_aux = {node for node in nodes}
        current, current_value = min(candidates, key=lambda x: x[1])
        current_value_aux = unvisited_aux[current]
    
    return parents, current_value, current_value_aux

def generate_path(parents, start , end):
    """
        Função que gera a rota entre dois pontos.
        parents -> dicionário com a rota mais curta
        start -> ponto de partida
        end -> ponto de chegada
        Retorna:
        path -> rota mais curta
    """
    path=[end]
    while True:
        key=parents[path[0]]
        path.insert (0, key)
        if key == start:
            break
    return " ---> ".join(path)

def cost_benefit(time, price, time_1, price_1, time_2, price_2):
    """
        Função que calcula o custo benefício da rota.
        time -> tempo do utilizador
        price -> preço do utilizador
        time_1 -> tempo da rota principal
        price_1 -> preço da rota principal
        time_2 -> tempo da rota auxiliar
        price_2 -> preço da rota auxiliar
        Retorna:
        1 -> custo benefício da rota 1
        2 -> custo benefício da rota 2
    """

    valor_base = time/price

    

    valor_1=abs(valor_base - (time_1)/(price_1))
    valor_2=abs(valor_base - (time_2)/(price_2))

    if valor_1 <= valor_2:
        return 1
    else:
        return 2


#Titulo pagina
st.title("Roteiro Europa: Melhor Transporte")

#Link para o grafo
st.html("<a href='https://aeeddipiaget.pt/grafo/' target='_blank'>Grafo</a>")

#Criar 2 colunas
col1, col2 = st.columns(2)

#Adicionar na coluna 1 a Origem
with col1:
    origem = st.selectbox("Origem", nodes)

#Adicionar na coluna 2 o Destino
with col2:
    destino = st.selectbox("Destino", nodes)

#Criterio de otimização
criterio = st.radio("Critério de otimização", ["time", "price", "time_price"], format_func=lambda x: "Tempo" if x == "time" else "Preço" if x == "price" else "Tempo e Preço")

#Declarar/Inicializar o tempo e preço
time, price = 0,0
if criterio == "time_price":
    #Criar 2 colunas
    col1, col2 = st.columns(2)

    #Adicionar na coluna 1 a Tempo
    with col1:
        time = st.text_input("Tempo(minutos)")

    #Adicionar na coluna 2 o Preço
    with col2:
        price = st.text_input("Preço(euros)")

if origem == destino:
    #Colocar aviso caso a origem e destino sejam iguais
    st.warning("A origem e o destino não podem ser iguais.")
elif time == "" or price == "" or time == "0" or price == "0":
    #Colocar aviso que tem de colocar o tempo e preço
    st.warning("Tem de colocar valores da relação tempo preço.")
else:
    if st.button("Calcular melhor transporte"):
        if criterio == "time_price":

            #Verificar se é melhor o tempo-preço ou o preço-tempo do carro
            parents_time, tempo_car_1, preco_car_1 = find_route_both(origem, destino, "time", "price", "car")
            parents_price, preco_car_2, tempo_car_2 = find_route_both(origem, destino, "price", "time", "car")
            if tempo_car_1 != tempo_car_2:
                if cost_benefit(int(time), int(price), tempo_car_1, preco_car_1, tempo_car_2, preco_car_2) == 1:
                    otimize_car = "time"
                    best_time_car, best_price_car = tempo_car_1, preco_car_1
                else:
                    otimize_car = "price"
                    best_time_car, best_price_car = tempo_car_2, preco_car_2
            elif preco_car_1 != preco_car_2:
                if cost_benefit(int(time), int(price), tempo_car_1, preco_car_1, tempo_car_2, preco_car_2) == 1:
                    otimize_car = "time"
                    best_time_car, best_price_car = tempo_car_1, preco_car_1
                else:
                    otimize_car = "price"
                    best_time_car, best_price_car = tempo_car_2, preco_car_2
            else:
                otimize_car = "time"
                best_time_car, best_price_car = tempo_car_1, preco_car_1

            #Verificar se é melhor o tempo-preço ou o preço-tempo do comboio
            parents_time, tempo_train_1, preco_train_1 = find_route_both(origem, destino, "time", "price", "train")
            parents_price, preco_train_2, tempo_train_2 = find_route_both(origem, destino, "price", "time", "train")
            if tempo_train_1 != tempo_train_2:
                if cost_benefit(int(time), int(price), tempo_train_1, preco_train_1, tempo_train_2, preco_train_2) == 1:
                    otimize_train = "time"
                    best_time_train, best_price_train = tempo_train_1, preco_train_1
                else:
                    otimize_train = "price"
                    best_time_train, best_price_train = tempo_train_2, preco_train_2
            elif preco_train_1 != preco_train_2:
                if cost_benefit(int(time), int(price), tempo_train_1, preco_train_1, tempo_train_2, preco_train_2) == 1:
                    otimize_train = "time"
                    best_time_train, best_price_train = tempo_train_1, preco_train_1
                else:
                    otimize_train = "price"
                    best_time_train, best_price_train = tempo_train_2, preco_train_2
            else:
                otimize_train = "time"
                best_time_train, best_price_train = tempo_train_1, preco_train_1

            #Verificar se é melhor o tempo-preço ou o preço-tempo do avião
            parents_time, tempo_plane_1, preco_plane_1 = find_route_both(origem, destino, "time", "price", "plane")
            parents_price, preco_plane_2, tempo_plane_2 = find_route_both(origem, destino, "price", "time", "plane")
            if tempo_plane_1 != tempo_plane_2:
                if cost_benefit(int(time), int(price), tempo_plane_1, preco_plane_1, tempo_plane_2, preco_plane_2) == 1:
                    otimize_plane = "time"
                    best_time_plane, best_price_plane = tempo_plane_1, preco_plane_1
                else:
                    otimize_plane = "price"
                    best_time_plane, best_price_plane = tempo_plane_2, preco_plane_2
            elif preco_plane_1 != preco_plane_2:
                if cost_benefit(int(time), int(price), tempo_plane_1, preco_plane_1, tempo_plane_2, preco_plane_2) == 1:
                    otimize_plane = "time"
                    best_time_plane, best_price_plane = tempo_plane_1, preco_plane_1
                else:
                    otimize_plane = "price"
                    best_time_plane, best_price_plane = tempo_plane_2, preco_plane_2
            else:
                otimize_plane = "time"
                best_time_plane, best_price_plane = tempo_plane_1, preco_plane_1

            #verificar se é melhor carro ou comboio
            if cost_benefit(int(time), int(price), best_time_car, best_price_car, best_time_train, best_price_train) == 1:
                #verificar se é melhor carro ou avião
                if cost_benefit(int(time), int(price), best_time_car, best_price_car, best_time_plane, best_price_plane) == 1:
                    meio = "Carro"
                else:
                    meio = "Avião"
            else:
                #Verificar se é melhor comboio ou avião
                if cost_benefit(int(time), int(price), best_time_train, best_price_train, best_time_plane, best_price_plane) == 1:
                    meio = "Comboio"
                else:
                    meio = "Avião"

            if meio == "Carro":
                #Colocar valores caso seja carro
                travel_type = "car"
                value_time = best_time_car
                value_price = best_price_car
                parents,x = find_route(origem, destino, otimize_car, "car")
            if meio == "Comboio":
                #Colocar valores caso seja Comboio
                travel_type = "train"
                value_time = best_time_train
                value_price = best_price_train
                parents,x = find_route(origem, destino, otimize_train, "train")
            if meio == "Avião":
                #Colocar valores caso seja Avião
                travel_type = "plane"
                value_time = best_time_plane
                value_price = best_price_plane
                parents,x = find_route(origem, destino, otimize_plane, "plane")

            #Criar o caminho de uma forma visualmente aceitavel
            path = generate_path(parents, origem, destino)
            
            #Colocar dados do melhor transporte
            st.success(f"Melhor meio de transporte: **{meio}**\n\n{path}\n\n{criterio.replace('_', ' + ').title()}: **{value_time // 60} horas e {value_time % 60} minutos ou {value_price:.2f} euros**")
            
            #Colocar tabela tempo
            show_table(f"Tempo - {meio} (minutos)", table_routes['time_' + travel_type])
            #Colocar tabela preço
            show_table(f"Preço - {meio} (€)", table_routes['price_' + travel_type])
        else:
            #Obter dados das viagens de carro, comboio e avião
            parents_car,car = find_route(origem, destino, criterio, "car")
            parents_train,train = find_route(origem, destino, criterio, "train")
            parents_plane,plane = find_route(origem, destino, criterio, "plane")
            #Verificar qual a menor
            if(car < train and car < plane):
                #Colocar valores caso seja carro
                travel_type = "car"
                meio = "Carro"
                valor = car
                parents = parents_car
            if(train < car and train < plane):
                #Colocar valores caso seja Comboio
                travel_type = "train"
                meio = "Comboio"
                valor = train
                parents = parents_train
            if(plane < car and plane < train):
                #Colocar valores caso seja Avião
                travel_type = "plane"
                meio = "Avião"
                valor = plane
                parents = parents_plane
            
            #Obter as unidades se é tempo ou preço
            unidade = f"{valor // 60} horas e {valor % 60} minutos" if criterio == "time" else f"{valor:.2f} euros"
            
            #Criar o caminho de uma forma visualmente aceitavel
            path = generate_path(parents, origem, destino)

            #Colocar dados do melhor transporte
            st.success(f"Melhor meio de transporte: **{meio}**\n\n{path}\n\n{criterio.capitalize()}: **{unidade}**")

            #Colocar tabela tempo
            show_table(f"Tempo - {meio} (minutos)" if criterio == "time" else f"Preço - {meio} (€)", table_routes[criterio + '_' + travel_type])

        #Colocar link para Google Maps
        st.html(f"<p>Verificar com dados reais:<a href='https://www.google.com/maps/dir/{nodes_lat_long[origem][0]},{nodes_lat_long[origem][1]}/{nodes_lat_long[destino][0]},{nodes_lat_long[destino][1]}' target='_blank'>Google Maps</a>")
