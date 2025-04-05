import string

def Imprimir_resultados(round):
    print("| Jugador   | Kills | Asistencias | Muertes | MVP  | Puntos |")
    print("-"*50)

    for fila in round:
        print(
            f"| {fila['Nombre']:<10}| {fila['Kills']:<6}| {fila['Assists']:<11}| "
            f"{fila['Death']:<6}| {fila['MVP']:<6}| {fila['Puntos']:<6}|"
        )
        print("-"*50)

def ordenar_jugadores(round):

    return sorted(round, key=lambda jugador: jugador['Puntos'], reverse=True)

def actualizar_estadisticas(round, stats_ronda, total, mvp_player):
   
    for player, stats in stats_ronda.items():
   
        total[player]['kills'] += stats['kills']
        total[player]['assists'] += stats['assists']
        total[player]['deaths'] += stats['deaths']
        total[player]['puntos'] += stats['puntos']

        if player == mvp_player:
            total[player]['mvp_count'] += 1  

        
        round.append({
            'Nombre': player,
            'Kills': total[player]['kills'],
            'Assists': total[player]['assists'],
            'Death': total[player]['deaths'],
            'MVP': total[player]['mvp_count'],  
            'Puntos': total[player]['puntos']
        })

def determinar_mvp(stats_ronda, round_data, mvp_player):
  
    max_puntos = -1 

    for player, stats in round_data.items():

        puntos = (stats['kills'] * 3) + stats['assists'] - (1 if stats['deaths'] else 0)
        
        
        stats_ronda[player] = {
            'kills': stats['kills'],
            'assists': stats['assists'],
            'deaths': 1 if stats['deaths'] else 0,
            'puntos': puntos
        }
        
   
        if puntos > max_puntos:
            max_puntos = puntos
            mvp_player = player
    
    return mvp_player


def cargar_rondas(rounds, total):
    
    ronda_num = 1
    
    for round_data in rounds:

        if ronda_num == 5:
            print("Ranking ronda Final")
        else:
            print(f"Ranking ronda {ronda_num}")
        
        ronda = []
        stats_ronda = {}
        mvp_player = None
        
        mvp_player = determinar_mvp(stats_ronda, round_data, mvp_player)
        
        actualizar_estadisticas(ronda, stats_ronda, total, mvp_player)
        ronda_ordenada = ordenar_jugadores(ronda)
        
        Imprimir_resultados(ronda_ordenada)
        
        ronda_num += 1
    


