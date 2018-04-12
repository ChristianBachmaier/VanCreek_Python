vc_string = "Christian Bachmaier";
vc_integer = 3;
vc_double = 4.0;
vc_bool = False;

vc_list = [1, 2, 3];
vc_sublist = [4, 5, 6];
vc_list = vc_list.__add__(vc_sublist);
print(vc_list);

if(vc_sublist.__len__() == 3):
    print("wahr") 
else:
    print("falsch"); 
