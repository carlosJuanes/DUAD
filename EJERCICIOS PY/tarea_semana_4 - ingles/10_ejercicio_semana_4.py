#10. Create an algorithm that asks the user for a speed in km/h and converts it to m/s.
#  Remember that 1 km = 1000m and 1 hour = 60 minutes * 60 seconds


speed_km_h=float(input( "please enter your speed in km/h = "))
speed_m_s=speed_km_h*1000/3600
print(f"your speed is  {speed_m_s:.2f} meter per seconds")