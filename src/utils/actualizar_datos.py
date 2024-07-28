import pandas as pd
def actualizar_datos(df, equipo, goles_a_favor, goles_en_contra):
    # Determinar el resultado del partido
    if goles_a_favor > goles_en_contra:
        puntos = 3
        won = 1
        drawn = 0
        lost = 0
    elif goles_a_favor == goles_en_contra:
        puntos = 1
        won = 0
        drawn = 1
        lost = 0
    else:
        puntos = 0
        won = 0
        drawn = 0
        lost = 1

    # Verificar si el equipo ya está en el DataFrame
    if equipo in df['id'].values:
        index = df[df['id'] == equipo].index[0]
        df.at[index, 'played'] += 1
        df.at[index, 'won'] += won
        df.at[index, 'drawn'] += drawn
        df.at[index, 'lost'] += lost
        df.at[index, 'points'] += puntos
        df.at[index, 'gf'] += goles_a_favor
        df.at[index, 'ga'] += goles_en_contra
        df.at[index, 'gd'] = df.at[index, 'gf'] - df.at[index, 'ga']
    else:
        # df = df.append({
        #     'id': equipo,
        #     'played': 1,
        #     'won': won,
        #     'drawn': drawn,
        #     'lost': lost,
        #     'gf': goles_a_favor,
        #     'ga': goles_en_contra,
        #     'gd': goles_a_favor - goles_en_contra,
        #     'points': puntos
        # }, ignore_index=True)


        df = pd.concat(
            [df, pd.DataFrame([{
                'id': equipo,
                'played': 1,
                'won': won,
                'drawn': drawn,
                'lost': lost,
                'gf': goles_a_favor,
                'ga': goles_en_contra,
                'gd': goles_a_favor - goles_en_contra,
                'points': puntos
            }])], ignore_index=True
        )
    return df
