from PIL import Image

n = 10000
recaman = [0]

for i in range(1, n+1):
	plusTarget = recaman[-1] + i
	subtTarget = recaman[-1] - i
	if subtTarget in recaman or subtTarget < 0:
		recaman.append(plusTarget)
	else:
		recaman.append(subtTarget)

N = max(recaman)

W = 1000
H = 1000

colorWhite = (255, 255, 255)
colorBlack = (0, 0, 0)

startPoint = (0, H-1)
endPoint = (W-1, 0)
segment = ((W-1)/N, ((H-1)/N)*-1)

def numToPoint(num):
	x, y = startPoint
	dx, dy = segment
	dx *= num
	dy *= num
	newPoint = (x+dx, y+dy)
	return newPoint

def drawNum2Num(im, numA, numB, direction):
	if numA > numB:
		numA, numB = numB, numA
	
	pA = numToPoint(numA)
	pB = numToPoint(numB)

	xa, ya = pA
	xb, yb = pB
	xa, xb, ya, yb = int(xa), int(xb), int(ya), int(yb)
	xc = xb if direction == 0 else xa
	yc = ya if direction == 0 else yb
	for xi in range(xa, xb):
		im.putpixel((xi, yc), colorBlack)
	for yi in range(yb, ya):
		im.putpixel((xc, yi), colorBlack)



im = Image.new('RGB', (W, H), colorWhite)


for i in range(len(recaman)-1):
	print(i, '/', n, end='\r')
	drawNum2Num(im, recaman[i], recaman[i+1], i % 2)

im.save('recaman.jpg')