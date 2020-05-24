a=90
b=5



c=a+b

accuracy=c



accuracy = int(accuracy)
f= open("accuracy.txt","w+")
f.write(str(accuracy))
f.close()
print("Accuracy for the model is : " , accuracy ,"%")
