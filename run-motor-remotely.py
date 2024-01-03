import rpyc

conn = rpyc.classic.connect('10.37.211.162')
motors = conn.modules['ev3dev2.motor']
m = motors.LargeMotor('outB')
m.run_timed(time_sp=1000, speed_sp=600)
