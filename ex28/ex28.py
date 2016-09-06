print ("1. True and True = %s" % str(True and True))
# Ture
print ("2. False and True = %s" % str(False and True))
# False
print ("3. 1 == 1 and 2 == 1 = %s" % str(1 == 1 and 2 == 1))
# False
print ('''4. test" == "test = %s''' % str("test" == "test"))
# Ture
print ("5. 1 == 1 or 2 != 1 = %s" % str(1 == 1 or 2 != 1))
# Ture
print ("6. True and 1 == 1 = %s" % str(True and 1 == 1))
# Ture
print ("7. False and 0 != 0 = %s" % str(False and 0!= 0))
# False
print ("8. True or 1 == 1 = %s" % str(True or 1 == 1))
# Ture
print ('''9. "test" == "testing" = %s''' % str("test" == "testing"))
# False
print ("10. 1 != 0 and 2 == 1 = %s" % str(1 != 0 and 2 == 1))
# False
print ('''11. "test" != "testing" = %s''' % str("test" != "testing"))
# Ture
print ('''12. "test" == 1 = %s''' % str("test" == 1))
# False
print ("13. not (True and False) = %s" % str((not (True and False))))
# Ture
print ("14. not (1 == 1 and 0 != 1) = %s" % str((not (1 == 1 and 0 != 1))))
# False
print ("15. not (10 == 1 or 1000 == 1000) = %s" % str((not (10 == 1 or 1000 == 1000))))
# Ture
print ("16. not (1 != 10 or 3 == 4) = %s" % str((not (1 != 10 or 3 == 4))))
# False
print ('''17. not ("testing" == "testing" and "Zed" == "Cool Guy") = %s''' % str((not ("testing" == "testing" and "Zed" == "Cool Guy"))))
# Ture
print ('''18. 1 == 1 and (not ("testing" == 1 or 1 == 0)) = %s''' % str(1 == 1 and (not ("testing" == 1 or 1 == 0))))
# Ture
print ('''19. "chunky" == "bacon" and (not (3 == 4 or 3 == 3)) = %s''' % str("chunky" == "bacon" and (not (3 == 4 or 3 == 3))))
# False
print ('''20. 3 == 3 and (not ("testing" == "testing" or "Python" == "Fun")) = %s''' % str(3 == 3 and (not ("testing" == "testing" or "Python" == "Fun"))))
# False

print ("extra 1. 'test' and 'test = = %s" % str('test' and 'test'))
# test
print ("extra 2. 1 and 1 = = %s" % str(1 and 1))
# 1
print ("extra 3. False and 1 = = %s" % str(False and 1))
# 1
print ("extra 4. Ture and 1 = = %s" % str(True and 1))
# 1