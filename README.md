ok deci in ultima varianta asta pusa sa o iei exact asa cum e sa nu o merge-ui cu alceva ca am facut legatura cu back ul prin login si pe scurt am facut frointul sa reactioneze la butoane 
am dus totodata la capat ideea ca managerul va fi din prima in baza noastra de date si el va fi in stare sa creeze conturi de manager
dar totodata ducem ideea ca va exista o singura pagina de login iar din introducerea de date ne vom da seama de ce rol este vorba manager sau staff
avem si chestia de creeare de cod qr insa momentan nu avem url ul pentru acesta dar suntem pe drumul drept si totul este ok

PENTRU ANTONIA !!!!!!!!!!!!!!!!!!!!!!11
in cazul in care mai vrei sa lucrezi poti sa incepi sa faci endpoint-urile pentru restul de poagini inafara de login adica:
Menu : trebuie sa ai mai multe metode ca managerul sa vada meniul actual totodata sa poate adauga dar sa si dea update la cel existent
Staff : asta e cam la fel cu cel de meniu doar ca e cu staff
MyOrders : asta sti ce face isi vede comenzile lui deci ai putea sa gandesti o functie eficienta de a cauta in baza de date comenzile semnate cu id-ul stafului
AllOrders : aici sa vada toate toate comenzile si sa le poata "semna" ca a le lui adica sa isi puna id ul pe ele

deci in mare cam asta e urmatorul pas totodata te rog sa ai in vedere faptul ca trebuie sa ne intalnim sa facem logica din spatele autentificarii pentru ca ar fi frumos si cinstit noi
fiind doi pe back sa ne ocupam de parte asta oferindui lui teo o sansa de a face si ea ceva frumos pe front 
