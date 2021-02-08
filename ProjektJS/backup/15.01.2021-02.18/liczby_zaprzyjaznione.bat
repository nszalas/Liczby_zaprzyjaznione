@echo off 

goto MENU
:MENU
cls
echo  +++++++++++++++++++++++++++++++++++++++++++++++++
echo                        MENU                      
echo  +++++++++++++++++++++++++++++++++++++++++++++++++
echo.                                   
echo                 1. Uruchom program                    
echo.                                   
echo               2. Wykonaj podsumowanie                
echo.
echo              3. Informacje o dzialaniu 
echo.                                 
echo                     4. Backup                  
echo.                                
echo                     5. Zakoncz                  
echo.                               
echo  +++++++++++++++++++++++++++++++++++++++++++++++++

set /p wybor="Wybierz opcje 1/2/3/4/5: "
If %wybor%==1 goto URUCHOM
If %wybor%==2 goto ZACZNIJ
If %wybor%==3 goto INFO
If %wybor%==4 goto BACKUP
If %wybor%==5 goto exit

:URUCHOM
cls
liczby_zaprzyjaznione.py
set /p wybor="Aby wrocic do MENU nacisnij ENTER..."
goto MENU

:ZACZNIJ
cls
LZ_tworzeniestrony.py
set /p wybor="Aby wrocic do MENU nacisnij ENTER..."
goto MENU

:INFO
cls
echo  +++++++++++++++++++++++++++++++++++++++++++++++++
echo               INFORMACJE O PROGRAMIE
echo  +++++++++++++++++++++++++++++++++++++++++++++++++
echo.
echo   Glownym celem programu jest sprawdzenie czy
echo   suma wszystkich dzielników pierwszej z liczb 
echo   równa się liczbie drugiej i na odwrót. 
echo.
echo   Aby program poprawnie zadzialal, kazda para 
echo   liczb musi znajdowac sie w osobnej linijce pliku
echo   tekstowego. Do tego liczby musza zostac 
echo   oddzielone spacja, ktora musi tez zostac dodana 
echo   za druga z nich. 
echo.
echo   Istnieje rowniez funkcja "Wykonaj podsumowanie"
echo   wyswietlajaca wyniki dla wczesniej uruchomionego 
echo   programu w postaci strony HTML.
echo.
echo.
echo   Program napisany przez Natalie Szalas.
echo.
echo.  
set /p wybor="Aby wrocic do MENU nacisnij ENTER..."
goto MENU


:BACKUP
set Day=%Date:~0,2%
set Mth=%Date:~3,2%
set Yr=%Date:~6,4%
set Hour=%Time:~0,2%
if "%hour:~0,1%" == " " set hour=0%hour:~1,1%
set Min=%Time:~3,2%
set name="%date%-%hour%.%min%"

cd..
mkdir "backup\%name%"
xcopy Projekt backup\%name% /E /I /H /Y

cls
echo  +++++++++++++++++++++++++++++++++++++++++++++++++
echo                        BACKUP                      
echo  +++++++++++++++++++++++++++++++++++++++++++++++++
echo.
echo.
echo   Backup zostal wykonany z data %name%
echo.
echo.
echo  +++++++++++++++++++++++++++++++++++++++++++++++++
echo.
set /p wybor="Aby wrocic do MENU nacisnij ENTER..."
goto MENU