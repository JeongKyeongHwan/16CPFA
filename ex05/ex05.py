name = 'Zed A. Shaw'
age = 23 # age
height_cm = 175 # centi meter
weight_kg = 75 # kg
eyes = 'Blue'
teeth = 'White'
hair = 'Brown'
#place holder
print "Let's talk about %s." % name
print "He's %d inches tall." % height_cm
print "He's %d pounds heavy." % weight_kg
print "Actually that's not too heavy."
print "He's got %s eyes and %s hair." % (eyes, hair)
print "His teeth are usually %s depending on the coffee." % teeth

# this line is tricky, try to get it exactly right
print "If I add %d, %d, and %d I get %d." % (
    age, height_cm, weight_kg, age + height_cm + weight_kg)

centi_meter = 2.54 # inches

print "%s * 10 inches = 25.4 inches." % centi_meter

print centi_meter * 10
