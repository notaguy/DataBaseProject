/*inserare in tabela cmd*/
insert into cmd values ('Boli si tulburari ale sistemului nervos',1);
insert into cmd values ('Boli si tulburari ale ochiului',2);
insert into cmd values ('Boli si tulburari ale sistemului respirator',3);
insert into cmd values ('Boli si tulburari ale sistemului circulator',4);
insert into cmd values ('Boli si tulburari ale sistemului digestiv',5);
insert into cmd values ('Boli si tulburari ale sistemului hepatobiliar si pancreasului',6);
insert into cmd values ('Boli si tulburari ale sistemului musculoscheletal si tesutului conjunctiv',7);
insert into cmd values ('Boli si tulburari ale glandelor endocrine si boli de nutritie',8);
insert into cmd values ('Boli si tulburari ale aparatului reproductiv',9);
insert into cmd values ('Boli ale sangelui',10);
insert into cmd values ('Boli infectioase si parazitare',11);
insert into cmd values ('Arsuri',12);
insert into cmd values ('Boli si tulburari ale pielii',13);
insert into cmd values ('Nou nascut',14);
insert into cmd values ('Sarcina si lauzie',15);
insert into cmd values ('Boli si tulburari mentale',16);

/*inserare in tabela specializari*/
insert into specializari (denumire, specializare_id) values ('Chirurgie cardiovasculara',1);
insert into specializari (denumire, specializare_id) values ('Neurologie',2);
insert into specializari (denumire, specializare_id) values ('Pneumologie',3);
insert into specializari (denumire, specializare_id) values ('Chirurgie generala',4);
insert into specializari (denumire, specializare_id) values ('Ortopedie si traumotologie',5);
insert into specializari (denumire, specializare_id) values ('Otorinolaringgologie',6); --ORL
insert into specializari (denumire, specializare_id) values ('Pediatrie',7);
insert into specializari (denumire, specializare_id) values ('Alergie si Imunologie',8);
insert into specializari (denumire, specializare_id) values ('Cardiologie',9);
insert into specializari (denumire, specializare_id) values ('Ginecologie',10);
insert into specializari (denumire, specializare_id) values ('Oncologie',11);
insert into specializari (denumire, specializare_id) values ('Medicina materna',12);
insert into specializari (denumire, specializare_id) values ('Endocrinologie',13);
insert into specializari (denumire, specializare_id) values ('Gastroenterologie',14);

/*inserare in tabela medic*/
insert into medic (nume, prenume, specializari_specializare_id) values ('Popescu', 'Marian', 1); 
insert into medic (nume, prenume, specializari_specializare_id) values ('Agafitei', 'Sergiu', 2); 
insert into medic (nume, prenume, specializari_specializare_id) values ('Budescu', 'George', 3); 
insert into medic (nume, prenume, specializari_specializare_id) values ('Potolea', 'Andreea', 3); 
insert into medic (nume, prenume, specializari_specializare_id) values ('Tihenea', 'Smaranda', 4); 
insert into medic (nume, prenume, specializari_specializare_id) values ('David', 'Laura', 5); 
insert into medic (nume, prenume, specializari_specializare_id) values ('Potoc', 'Bianca', 6); 
insert into medic (nume, prenume, specializari_specializare_id) values ('Palade', 'Roxana', 7); 
insert into medic (nume, prenume, specializari_specializare_id) values ('Ostricov', 'Paul', 8);
insert into medic (nume, prenume, specializari_specializare_id) values ('Craciun', 'Rares', 9); 
insert into medic (nume, prenume, specializari_specializare_id) values ('Budescu', 'Larisa', 10); 
insert into medic (nume, prenume, specializari_specializare_id) values ('Constantin', 'Eugen', 12);
insert into medic (nume, prenume, specializari_specializare_id) values ('David', 'Jana', 14); 

/*inserare in tabela pacient*/
insert into pacient (nume, prenume, varsta, gen, telefon, email) values ('Barcan', 'Nicoleta', 21, 'F', '0727785753', 'barcannicoleta@gmail.com');
insert into pacient (nume, prenume, varsta, gen, telefon, email) values ('Cumpat', 'Alexandru', 23, 'M', '0724568921', 'cumpata@yahoo.com');
insert into pacient (nume, prenume, varsta, gen, telefon, email) values ('Cazanel', 'Marius', 23, 'M', '0741478356', 'cazamarius@gmail.com');
insert into pacient (nume, prenume, varsta, gen, telefon, email) values ('Simioniuc', 'Ruxandra', 26, 'F', '0725649153', 'ruxandrasimionuc@gmail.com');
insert into pacient (nume, prenume, varsta, gen, telefon) values ('Munteanu', 'Ariadna', 19, 'F', '0735689730');
insert into pacient (nume, prenume, varsta, gen, telefon, email) values ('Apetrei', 'Octav', 32, 'M', '0721345689', 'apepatru@gmail.com');
insert into pacient (nume, prenume, varsta, gen, telefon, email) values ('Darie', 'Sergiu', 17, 'M', '0758364089', 'frostbyte@gmail.com');
insert into pacient (nume, prenume, varsta, gen, telefon) values ('Besu', 'Dan', 45, 'M', '0775469823');
insert into pacient (nume, prenume, varsta, gen, telefon, email) values ('Frangulea', 'Nerina', 21, 'F', '0768403591', 'frang.nerina@gmail.com');
insert into pacient (nume, prenume, varsta, gen, telefon, email) values ('Petrescu', 'Luminita', 55, 'F', '0736617922', 'luminitapetre@yahoo.com');

/*inserare in tabela istoric_initial*/
insert into istoric_initial (boli_anterioare, alergii, pacient_pacient_id) values ('gastrita si bronsita', 'la capsuni', 1);
insert into istoric_initial (alergii, pacient_pacient_id) values ('la soia', 7);
insert into istoric_initial (boli_anterioare, tratament_curent, pacient_pacient_id) values ('astm bronsic' ,'inhalator si corticosteroizi inhalatori', 4);
insert into istoric_initial (boli_anterioare, alergii, tratament_curent, pacient_pacient_id) values ('otita acuta externa difuza', 'la nuci', 'mesa cu rivanol, amoxacilina 1g la 12 ore', 10);
insert into istoric_initial (alergii, pacient_pacient_id) values ('rivanol', 2);
insert into istoric_initial (tratament_curent, pacient_pacient_id) values ('2 pastile de nedis', 3);
insert into istoric_initial (boli_anterioare, pacient_pacient_id) values ('hipertensiune', 6);
insert into istoric_initial (boli_anterioare, pacient_pacient_id) values ('colesterol marit', 8);
insert into istoric_initial (boli_anterioare, tratament_curent, pacient_pacient_id) values ('fractura de tibie', 'augmentin la 6 ore' , 9);

/*inserare in tabela programare*/
insert into programare (data_ora, etaj, sala, serviciu, pacient_pacient_id, medic_medic_id) values (TO_DATE('17-01-2023 12:00','DD-MM-YYYY HH24:MI'), 1, 6, 'consult', 1, 4);
insert into programare (data_ora, etaj, sala, serviciu, pacient_pacient_id, medic_medic_id) values (TO_DATE('17-01-2023 14:30','DD-MM-YYYY HH24:MI'), 0, 1, 'control', 2, 1);
insert into programare (data_ora, etaj, sala, serviciu, pacient_pacient_id, medic_medic_id) values (TO_DATE('20-02-2023 09:00','DD-MM-YYYY HH24:MI'), 0, 5, 'control', 3, 2);
insert into programare (data_ora, etaj, sala, serviciu, pacient_pacient_id, medic_medic_id) values (TO_DATE('20-02-2023 12:30','DD-MM-YYYY HH24:MI'), 2, 12, 'ecografie', 4, 12);
insert into programare (data_ora, etaj, sala, serviciu, pacient_pacient_id, medic_medic_id) values (TO_DATE('01-03-2023 08:00','DD-MM-YYYY HH24:MI'), 2, 11, 'rmn', 5, 9);
insert into programare (data_ora, etaj, sala, serviciu, pacient_pacient_id, medic_medic_id) values (TO_DATE('01-03-2023 10:30','DD-MM-YYYY HH24:MI'), 3, 18, 'ecografie', 6, 9);
insert into programare (data_ora, etaj, sala, serviciu, pacient_pacient_id, medic_medic_id) values (TO_DATE('01-03-2023 12:20','DD-MM-YYYY HH24:MI'), 2, 14, 'ecografie', 7, 13);
insert into programare (data_ora, etaj, sala, serviciu, pacient_pacient_id, medic_medic_id) values (TO_DATE('01-03-2023 14:00','DD-MM-YYYY HH24:MI'), 0, 1, 'analize', 8, 8);
insert into programare (data_ora, etaj, sala, serviciu, pacient_pacient_id, medic_medic_id) values (TO_DATE('01-03-2023 15:20','DD-MM-YYYY HH24:MI'), 1, 8, 'control', 9, 3);
insert into programare (data_ora, etaj, sala, serviciu, pacient_pacient_id, medic_medic_id) values (TO_DATE('02-03-2023 09:30','DD-MM-YYYY HH24:MI'), 1, 10, 'consult', 10, 2);
insert into programare (data_ora, etaj, sala, serviciu, pacient_pacient_id, medic_medic_id) values (TO_DATE('02-03-2023 12:00','DD-MM-YYYY HH24:MI'), 0, 1, 'control', 2, 10);

/*inserare in tabela diagnostic*/
insert into diagnostic (denumire, detalii, simptome, programare_programare_id, cmd_cmd_id) values ('Afectiunile nervilor', 'Nevralgia de trigemen', 'atacuri spontane de durere la mestecare, atingerea fetei sau vorbit', 3, 1);
insert into diagnostic (denumire, detalii, simptome, programare_programare_id, cmd_cmd_id) values ('Boli demielinizante ale sistemului nervos central', 'Scleroza difuza', 'atacuri ischemice tranzitorii de paloare ?i hiperemie, ca raspuns la frig sau stres emotional', 10, 1);
insert into diagnostic (denumire, detalii, simptome, programare_programare_id, cmd_cmd_id) values ('Cardiopatie reumatismala', 'Insuficienta aortica reumatismata', 'dificultati de respiratie, puls neregulat, durere toracica', 2, 4);
insert into diagnostic (denumire, detalii, simptome, programare_programare_id, cmd_cmd_id) values ('Gripa si pneumonie', 'Pneumonia cu adenovirusi', 'tuse productiva, febra, greata, fara apetit ', 9, 3);
insert into diagnostic (denumire, detalii, simptome, programare_programare_id, cmd_cmd_id) values ('Afectiuni ale sistemului respirator', 'Insuficienta respiratorie acuta', 'oboseala, greata, tuse ', 1, 3);
insert into diagnostic (denumire, detalii, simptome, programare_programare_id, cmd_cmd_id) values ('Malnutritia', 'Malnutritia proteino-energetica usoara', 'Pierderea pilozitatii corporale, piele uscata si fanere friabile', 8, 8);
insert into diagnostic (denumire, detalii, simptome, programare_programare_id, cmd_cmd_id) values ('Intoleranta la glucoza', 'Reglementarea intolerantei la glucoza cu angiopatie periferica cu gangrena', 'constipatie, dureri stomacale', 5, 8);
insert into diagnostic (denumire, detalii, simptome, programare_programare_id, cmd_cmd_id) values ('Reumatism articular', 'Reumatismul articular acut fara mentionarea complicatiilor cardiace', 'febra, amigdalite marite, dureri de cap', 6, 4);
insert into diagnostic (denumire, detalii, programare_programare_id, cmd_cmd_id) values ('Complicatii legate in principal de lauzie', 'Tromboflebita superficiala in timpul lauziei', 4, 15);
insert into diagnostic (denumire, detalii, simptome, programare_programare_id, cmd_cmd_id) values ('Hernia', 'Hernia ombilicala fara obstructie sau gangrena', 'senzatie de plenitudine, dureri in timpul ridicarii greutatilor ', 7, 5);
insert into diagnostic (denumire, detalii, simptome, programare_programare_id, cmd_cmd_id) values ('Cardiopatie reumatismala', 'Insuficienta aortica reumatismata', 'dificultati de respiratie, puls neregulat, durere toracica', 11, 4);

/*inserare in tabela tratament*/
insert into tratament values ('aspirina', 2, 'la 6 ore', '12 zile', 1);
insert into tratament values ('Mydocalm fiole', 1, 'pe zi, dupa masa', '3 luni', 2);
insert into tratament values ('orice vasodilactor', 2, 'dimineata si seara dupa mese', 'toata viata', 3);
insert into tratament values ('amoxacilina', 2, 'la 12 ore', '10 zile', 4);
insert into tratament values ('sport si ceai', null, 'zilnic', 'zilnic', 5);
insert into tratament values ('complex vitamine', 1, 'dimineata', '1 luna da una nu', 6);
insert into tratament values ('Gluten digest', 1, 'inainte de masa', '4 luni', 7);
insert into tratament values ('Artro Curcumin', 2, 'una pe zi', '3 saptamani', 8);
insert into tratament values ('Diolex', 1, 'la 12 ore', 'pe durata sarcinii', 9);
insert into tratament values ('odihna', null, 'zilnic', '3 luni repaos la pat', 10);
insert into tratament values ('Tolperisona', 1, 'pe zi, inainte masa', '2 luni', 11);
insert into tratament values ('Tolperisona', 2, 'la 12 ore, inainte masa', '2 luni', 11);
























