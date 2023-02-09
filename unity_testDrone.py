from DRONE import Drone
from DroneSocket import Server
import sys, time, os, threading
from dronekit import connect, VehicleMode
import time

drone = None
server = None

def main():
    global drone, server

    drone = Drone()
    drone.Connect()
    drone.Start()

    server = Server()
    server.set_target = drone.set_target
    server.Start()

    main_thread = threading.Thread(target=run)
    main_thread.start()

def run():
    global drone

    while True:
        try:
            continue
            #print(get_time_str() + get_drone_str(), end='\r')
            
        except KeyboardInterrupt:
            print("\nEXIT")
            os._exit(0)
        except:
            raise
        time.sleep(10)

def get_time_str():
    curr_time = int(round(time.time() * 100))
    return " Time: [{:6d}]".format(curr_time)

def get_drone_str():
    global drone

    return(" Velocity Received (SOLO): [x(forward){:6.2f}, y(Left){:6.2f}, z(up){:6.2f}] Yaw Received (SOLO): {:6.2f}".format(drone.target_velocity[2], drone.target_velocity[0], drone.target_velocity[1], drone.target_yaw))
    #if drone.vehicle.location.local_frame.north is not None:
        #return(" Position (SOLO): [x(forward){:6.2f}, y(left){:6.2f}, z(up){:6.2f}] Yaw (SOLO): {:6.2f}".format(drone.vehicle.location.local_frame.north,-drone.vehicle.location.local_frame.east,-drone.vehicle.location.local_frame.down, drone.vehicle.attitude.yaw))
    #else:
        #return(" Position (SOLO): [x(forward){:6s}, y(left){:6s}, z(up){:6s}]".format("N/A", "N/A", "N/A"))
    #     print(" Position (NED): {:4f}".format(drone.vehicle.location.local_frame.north, ), end='\r')
    # print(zed.get_translation(), end='\r')

if __name__ == "__main__":
    main()

