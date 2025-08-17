#10 Cree un algoritmo que le pida al usuario una velocidad en km/h y 
# la convierta a m/s. Recuerda que 1 km == 1000m y 1 hora == 60 minutos * 60 segundos.


velocidad_km_h=float(input( "ingrese su velocidad en km/h = "))
velocidad_m_s=velocidad_km_h*1000/3600
print(f"su velocidad es de {velocidad_m_s:.2f} metros por segundos")