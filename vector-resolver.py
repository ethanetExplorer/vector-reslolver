import math

yy = 10

while yy == 10:
    forceP = int(input("Enter force P here: "))
    forceQ = int(input("Enter force Q here: "))
    
    angleTheta = int(input("Enter angle theta here: "))
    angleThetaRad = angleTheta/180 * math.pi

    angleAlpha = int(input("Enter angle alpha here: "))
    angleAlphaRad = angleAlpha/180 * math.pi

    resultantForceX = (forceQ*-1*math.cos(angleAlphaRad)) + (forceP*math.cos(angleThetaRad)) 
    resultantForceY = (forceQ*math.sin(angleAlphaRad)) + (forceP*math.sin(angleThetaRad))

    resultantForce = (resultantForceX**2 + resultantForceY**2)**0.5

    print("")
    print("Resultant force in X direction: " + str(round(resultantForceX)))
    print("Resultant force in Y direction: " + str(round(resultantForceY)))
    print("Resultant force: " + str(round(resultantForce)))
    print("Angle: " + str(round(math.degrees(math.atan(abs(resultantForceY)/abs(resultantForceX))))))
      
