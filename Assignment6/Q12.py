# 12. Write a python script to accept one complex number from the user and display the
# greater number between real part and imaginary part.

a = complex(input("Enter complex num : "))
if a.real > a.imag:
    print(a.real, "real num is greater")
else:
    print(a.imag, "imaginary num is greater")

# print('Real : ', a.real, '\nImaginary : ', a.imag)
