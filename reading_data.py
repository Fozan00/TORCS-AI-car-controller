

def read_data(filename):
    file = open(filename, "r")
    main_list = []
    for val in range(1000):
        list1 = []
        st_len = len(str)
        index1 = str.find('angle', 0)
        index2 = str.find(']', index1)
        angle = ''
        for i in range(index1 + 8, index2):
            angle += str[i]
        list1.append(float(angle))
        ########################################
        index1 = str.find('curLapTime', index2)
        index2 = str.find(']', index1)
        curLapTime = ''
        for i in range(index1 + 13, index2):
            curLapTime += str[i]
        list1.append(float(curLapTime))
        ########################################
        index1 = str.find('damage', index2)
        index2 = str.find(']', index1)
        damage = ''
        for i in range(index1 + 9, index2):
            damage += str[i]
        list1.append(float(damage))
        ########################################
        index1 = str.find('distFromStart', index2)
        index2 = str.find(']', index1)
        distFromStart = ''
        for i in range(index1 + 16, index2):
            distFromStart += str[i]
        list1.append(float(distFromStart))
        ########################################
        index1 = str.find('distRaced', index2)
        index2 = str.find(']', index1)
        distRaced = ''
        for i in range(index1 + 12, index2):
            distRaced += str[i]
        list1.append(float(distRaced))
        #######################################
        index1 = str.find('fuel', index2)
        index2 = str.find(']', index1)
        fuel = ''
        for i in range(index1 + 7, index2):
            fuel += str[i]
        list1.append(float(fuel))
        ########################################
        index1 = str.find('gear', index2)
        index2 = str.find(']', index1)
        gear = ''
        for i in range(index1 + 7, index2):
            gear += str[i]
        list1.append(float(gear))
        ########################################
        index1 = str.find('lastLapTime', index2)
        index2 = str.find(']', index1)
        lastLapTime = ''
        for i in range(index1 + 14, index2):
            lastLapTime += str[i]
        list1.append(float(lastLapTime))
        ########################################
        index1 = str.find('racePos', index2)
        index2 = str.find(']', index1)
        racePos = ''
        for i in range(index1 + 10, index2):
            racePos += str[i]
        list1.append(float(racePos))
        ########################################

        index1 = str.find('rpm', index2)
        index2 = str.find(']', index1)
        rpm = ''
        for i in range(index1 + 6, index2):
            rpm += str[i]
        list1.append(float(rpm))
        ########################################
        index1 = str.find('speedX', index2)
        index2 = str.find(']', index1)
        speedX = ''
        for i in range(index1 + 9, index2):
            speedX += str[i]
        list1.append(float(speedX))
        ########################################
        index1 = str.find('speedY', index2)
        index2 = str.find(']', index1)
        speedY = ''
        for i in range(index1 + 9, index2):
            speedY += str[i]
        list1.append(float(speedY))
        ########################################
        index1 = str.find('speedZ', index2)
        index2 = str.find(']', index1)
        speedZ = ''
        for i in range(index1 + 9, index2):
            speedZ += str[i]
        list1.append(float(speedZ))
        ########################################
        index1 = str.find('track', index2)
        index2 = str.find(',', index1)
        track0 = ''
        for i in range(index1 + 8, index2):
            track0 += str[i]
        list1.append(float(track0))
        ########################################
        index1 = index2 + 2
        index2 = str.find(',', index1)
        track1 = ''
        for i in range(index1, index2):
            track1 += str[i]
        list1.append(float(track1))
        ########################################
        index1 = index2 + 2
        index2 = str.find(',', index1)
        track2 = ''
        for i in range(index1, index2):
            track2 += str[i]
        list1.append(float(track2))
        ########################################
        index1 = index2 + 2
        index2 = str.find(',', index1)
        track3 = ''
        for i in range(index1, index2):
            track3 += str[i]
        list1.append(float(track3))
        ########################################
        index1 = index2 + 2
        index2 = str.find(',', index1)
        track4 = ''
        for i in range(index1, index2):
            track4 += str[i]
        list1.append(float(track4))
        ########################################
        index1 = index2 + 2
        index2 = str.find(',', index1)
        track5 = ''
        for i in range(index1, index2):
            track5 += str[i]
        list1.append(float(track5))
        ########################################
        index1 = index2 + 2
        index2 = str.find(',', index1)
        track6 = ''
        for i in range(index1, index2):
            track6 += str[i]
        list1.append(float(track6))
        ########################################
        index1 = index2 + 2
        index2 = str.find(',', index1)
        track7 = ''
        for i in range(index1, index2):
            track7 += str[i]
        list1.append(float(track7))
        ########################################
        index1 = index2 + 2
        index2 = str.find(',', index1)
        track8 = ''
        for i in range(index1, index2):
            track8 += str[i]
        list1.append(float(track8))
        ########################################
        index1 = index2 + 2
        index2 = str.find(',', index1)
        track9 = ''
        for i in range(index1, index2):
            track9 += str[i]
        list1.append(float(track9))
        ########################################
        index1 = index2 + 2
        index2 = str.find(',', index1)
        track10 = ''
        for i in range(index1, index2):
            track10 += str[i]
        list1.append(float(track10))
        ########################################
        index1 = index2 + 2
        index2 = str.find(',', index1)
        track11 = ''
        for i in range(index1, index2):
            track11 += str[i]
        list1.append(float(track11))
        ########################################
        index1 = index2 + 2
        index2 = str.find(',', index1)
        track12 = ''
        for i in range(index1, index2):
            track12 += str[i]
        list1.append(float(track12))
        ########################################
        index1 = index2 + 2
        index2 = str.find(',', index1)
        track13 = ''
        for i in range(index1, index2):
            track13 += str[i]
        list1.append(float(track13))
        ########################################
        index1 = index2 + 2
        index2 = str.find(',', index1)
        track14 = ''
        for i in range(index1, index2):
            track14 += str[i]
        list1.append(float(track14))
        ########################################
        index1 = index2 + 2
        index2 = str.find(',', index1)
        track15 = ''
        for i in range(index1, index2):
            track15 += str[i]
        list1.append(float(track15))
        ########################################
        index1 = index2 + 2
        index2 = str.find(',', index1)
        track16 = ''
        for i in range(index1, index2):
            track16 += str[i]
        list1.append(float(track16))
        ########################################
        index1 = index2 + 2
        index2 = str.find(',', index1)
        track17 = ''
        for i in range(index1, index2):
            track17 += str[i]
        list1.append(float(track17))
        ########################################
        index1 = index2 + 2
        index2 = str.find(']', index1)
        track18 = ''
        for i in range(index1, index2):
            track18 += str[i]
        list1.append(float(track18))
        ########################################
        index1 = str.find('trackPos', index2)
        index2 = str.find(']', index1)
        trackPos = ''
        for i in range(index1 + 11, index2):
            trackPos += str[i]
        list1.append(float(trackPos))
        ########################################
        index1 = str.find('wheelSpinVel', index2)
        index2 = str.find(',', index1)
        wheelSpinVel0 = ''
        for i in range(index1 + 15, index2):
            wheelSpinVel0 += str[i]

        list1.append(float(wheelSpinVel0))
        ########################################
        index1 = index2 + 2
        index2 = str.find(',', index1)
        wheelSpinVel1 = ''
        for i in range(index1, index2):
            wheelSpinVel1 += str[i]
        list1.append(float(wheelSpinVel1))
        ########################################
        index1 = index2 + 2
        index2 = str.find(',', index1)
        wheelSpinVel2 = ''
        for i in range(index1, index2):
            wheelSpinVel2 += str[i]
        list1.append(float(wheelSpinVel2))
        ########################################
        index1 = index2 + 2
        index2 = str.find(']', index1)
        wheelSpinVel3 = ''
        for i in range(index1, index2):
            wheelSpinVel3 += str[i]
        list1.append(float(wheelSpinVel3))
        ########################################

        index1 = str.find('accel', index2)
        index2 = str.find(')', index1)
        accel = ''
        for i in range(index1 + 6, index2):
            accel += str[i]
        list1.append(float(accel))
        index1 = str.find('steer', index2)
        index2 = str.find(')', index1)
        steer = ''
        for i in range(index1 + 6, index2):
            steer += str[i]
        list1.append(float(steer))

        main_list.append(list1)
    return main_list

