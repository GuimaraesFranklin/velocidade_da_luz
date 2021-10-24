# Este programa visa calular a distancia em kms para a velocidade da luz

light_velocity = 299792458

light_year = float(input('Quantos anos luz: '))

light_velocity = light_velocity * 60
light_velocity = light_velocity * 60
light_velocity = light_velocity * 24
light_velocity = light_velocity * 365

distance = light_velocity * light_year

print(
    f'A distancia percorrida em {light_year} anos/luz é de {distance} kms')
