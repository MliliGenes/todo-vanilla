# import math
# class Vecteur3d :
#     id = 0
#     def __init__(self,x=0,y=0,z=0):
#         self.__x = x
#         self.__y = y
#         self.__z = z
#         Vecteur3d.id+= 1

#     def getX(self):
#         return self.__x
#     def getY(self):
#         return self.__y
#     def getZ(self):
#         return self.__z

#     def setX(self,x):
#         self.__x = x
#     def setY(self, y):
#         self.__y = y
#     def setZ(self,z):
#         self.__z = z

#     def __str__(self):
#         return f"<{self.__x},{self.__y},{self.__z}>"
    
#     def normeVecteur(self):
#         return (f'{math.sqrt(self.__x**2+self.__y**2+self.__z**2):.2f}')

#     @staticmethod
#     def sommeVec(v1,v2):
#         v = Vecteur3d()
#         v.__x = v1.__x + v2.__x
#         v.__y = v1.__y + v2.__y
#         v.__z = v1.__z + v2.__z
#         return v
    
#     def ProduitS(self,V):
#         return self.__x*V.__x+self.__y*V.__y+self.__z*V.__z

# vecteur1 = Vecteur3d(5,2,8)
# print(Vecteur3d.id)
# print(vecteur1.normeVecteur())
# vecteur2 = Vecteur3d(6,4,7)
# print(Vecteur3d.id)
# print(vecteur2.normeVecteur())
# vecteur3 = Vecteur3d(8,10,2)
# print(Vecteur3d.id)
# print(vecteur3.normeVecteur())
# vecteur4 = Vecteur3d.sommeVec(vecteur1,vecteur3)
# print(vecteur1.ProduitS(vecteur2))



# class Client:
    
#     def __init__(self,code=0,nom="",address=""):
#         self.__code = code
#         self.__nom = nom
#         self.__address = address
    
#     @property
#     def Code(self):
#         return self.__code
#     @Code.setter
#     def Code(self,code):
#         self.__code = code
#     @property
#     def Nom(self):
#         return self.__nom
#     @Nom.setter
#     def Nom(self,nom):
#         self.__nom = nom
#     @property
#     def Address(self):
#         return self.__address
#     @Address.setter
#     def Address(self,address):
#         self.__address = address
    
#     def __str__(self):
#         return f'{self.Nom};{self.Code};{self.Address}'

#     def equals(self,c2):
#         return self.__nom == c2.__nom and self.__code == c2.__code

# clientsList=[]
# while True:
#     print("""
# menu:
# 1 - add
# 2 - show
# 3 - delete
# 4 - search
# 5 - update
# 6 - quite""")
#     choice = int(input('enter your choice : '))
#     if choice == 6 :
#         break
#     elif choice == 1:
#         C = Client(int(input("Code : ")),
#                 input("Nom : "),
#                 input("address : "))
#         clientsList.append(C)
#     elif choice == 2:
#         if clientsList :
#             for i in clientsList:
#                 print(i)
#     elif choice == 3:
#         if clientsList :
#             c = int(input('code ? : '))
#             exist = False
#             for i in clientsList:
#                 if i.Code == c:
#                     clientsList.remove(i)
#                     exist = True
#                     break
#             if not exist:
#                 print('this client doesnt exist')
#     elif choice == 4:
#         if clientsList :
#             c = int(input('code ? : '))
#             exist = False
#             for i in clientsList:
#                 if i.Code == c:
#                     print(i)
#                     exist = True
#                     break
#             if not exist:
#                 print('this client doesnt exist')
#     elif choice == 3:
#         if clientsList :
#             c = int(input('code ? : '))
#             exist = False
#             for i in clientsList:
#                 if i.Code == c:
#                     i.Address = input('new address : ')
#                     exist = True
#                     break
#             if not exist:
#                 print('this client doesnt exist')


# class Fournisseur :
#     def __init__(self,c=0,n="",a=""):
#         self.__nom = n
#         self.__code = c
#         self.__address = a
#     @property
#     def Code(self):
#         return self.__code
#     @Code.setter
#     def Code(self,c):
#         self.__code = c
#     @property
#     def Nom(self):
#         return self.__nom
#     @Nom.setter
#     def Nom(self,n):
#         self.__nom = n
#     @property
#     def Address(self):
#         return self.__address
#     @Address.setter
#     def Address(self,a):
#         self.__address = a
#     def __str__(self):
#         return f'Code : {self.Code},Nom : {self.Nom},Address : {self.Address}'
#     def Equals(self,obj):
#         return self.Code == obj.Code and self.Nom == obj.Nom

# class Produit:
#     def __init__(self,d="",p=0,f=Fournisseur()):
#         self.__designation = d
#         self.__prix = p
#         self.__fournisseur = f
#     @property
#     def Designation(self):
#         return self.__designation
#     @Designation.setter
#     def Designation(self,d):
#         self.__designation = d
        
#     @property
#     def Prix(self):
#         return self.__prix
#     @Prix.setter
#     def Prix(self,p):
#         self.__prix = p
        
#     @property
#     def Fournisseur(self):
#         return self.__fournisseur
#     @Fournisseur.setter
#     def Fournisseur(self,f):
#         self.__fournisseur = f
    
#     def __str__(self):
#         return f"Designation : {self.Designation},Prix : {self.Prix},Fournisseur : {self.Fournisseur}"

# proctsList = []

# while True:
#     print("""
# menu:
# 1 - show
# 2 - add
# 3 - delete
# 4 - search
# 6 - quite""")
#     choice = int(input('choice : '))
#     if choice == 6:
#         break
#     elif choice == 1:
#         if proctsList :
#             for i in proctsList:
#                 print(i)
#     elif choice == 2:
#         proctsList.append(Produit(input('d'),int(input('n')),Fournisseur()))
#     elif choice == 4:
#         if proctsList :
#             d = int(input('d : '))
#             flag = False
#             for i in proctsList:
#                 if i.Designation == d:
#                     proctsList.remove(i)
#                     flag = True
#                     break
#             if not flag:
#                 print('doesnt exist')
#     elif choice == 2:
#         if proctsList :
#             d = int(input('d : '))
#             flag = False
#             for i in proctsList:
#                 if i.Designation == d:
#                     proctsList.remove(i)
#                     flag = True
#                     break
#             if not flag:
#                 print('doesnt exist')


class Auteur:
    
    def __init__(self,name="",natio=""):
        self.__name = name
        self.__nationalite = natio

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self,new_name):
        self.__name = new_name
        
    @property
    def natio(self):
        return self.__nationalite
    
    @natio.setter
    def natio(self,new_natio):
        self.__nationalite = new_natio
    
    def __str__(self) :
        return f"name : {self.name}, nationalite : {self.natio}"

class Liver:
    
    def __init__(self,name='',editor="",nombre=0,list=[]):
        self.__name = name
        self.__editor = editor
        self.__nombre = nombre
        self.__list = list
    
    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self,new_name):
        self.__name = new_name
        
    @property
    def editor(self):
        return self.__editor
    
    @editor.setter
    def editor(self,new_editor):
        self.__editor = new_editor
    
    @property
    def nombre(self):
        return self.__nombre
    
    @nombre.setter
    def nombre(self,new_nombre):
        self.__nombre = new_nombre

    @property
    def list(self):
        return self.__list
    
    @list.setter
    def list(self,new_list):
        self.__list = new_list
    
    def AfficheAuteursLivres(self):
        for i in self.list:
            print(i)
    
    def AjouterAuteur(self,auteur):
        if auteur in self.list:
            print('auteur exist!')
        else:
            if isinstance(auteur,Auteur):
                self.list.append(auteur)
            else:
                print("this is not an obj!")
    
    def Ajouter(self):
        nom = input("nom : ")
        nat = input("nat : ")
        a = Auteur(nom,nat)
        if a not in self.list:
            self.list.append(a)
    
    def Supprimer(self,auteur):
        self.list.remove(auteur) if auteur in self.list else print("saad")
    
    def SupprimerName(self,a):
        flag = False
        for i in self.list:
            if i.name == a:
                self.list.remove(i)
                flag = True
                break
        if not flag:
            print("omg")
    
    def __str__(self):
        saad= ''
        for i in self.list:
            saad += str(i) + "\n"
        return f'name : {self.name}, editor : {self.editor}, pages : {self.nombre}, auteurs : {saad}'

class Biblio:
    def __init__(self,name="",address="",list=[]):
        self.__name = name
        self.__address = address
        self.__list = list

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self,new_name):
        self.__name = new_name
        
    @property
    def address(self):
        return self.__address
    
    @address.setter
    def address(self,new_address):
        self.__address = new_address
        
    @property
    def list(self):
        return self.__list
    
    @list.setter
    def list(self,new_list):
        self.__list = new_list

    def AfficheLivreBiblio(self):
        for i in self.list:
            print(i)
    
    def AjouterLivre(self, book):
        if book in self.list:
            print('book exist!')
        else:
            if isinstance(book,Liver):
                self.list.append(book)
            else:
                print("this is not an obj!")
    
    def Ajouter(self):
        nom = input("nom : ")
        nombre = input("nombre : ")
        editor = input("editor : ")
        a = Liver(nom,editor,nombre)
        pj = int(input("haha ha ha"))
        for i in range(pj):
            a.Ajouter()
        