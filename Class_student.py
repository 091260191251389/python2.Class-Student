class Student():
    f_n = str(input("Enter your first name :"))
    l_n = str(input("Enter your last name :"))
    age = float(input("Enter your age :"))
    m_s = float(input("Enter your math score :"))
    p_s = float(input("Enter your physics score :"))
    py_s = float(input("Enter your python score :"))

    def Chek_status():
        if m_s + p_s + py_s <= 17:
            x = str(input("Do you want see the scores avrage ?"))
            if x == 'yes':
                print((m_s + p_s + py_s)/3)
            else x == 'no':
        else :
            print('Failed')