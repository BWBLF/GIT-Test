
# bitmap

from operator import index


bitmap = """
14. ....................................................................
15.    **************   *  *** **  *      ******************************
16.   ********************* ** ** *  * ****************************** *
17.  **      *****************       ******************************
18.           *************          **  * **** ** ************** *
19.            *********            *******   **************** * *
20.             ********           ***************************  *
21.    *        * **** ***         *************** ******  ** *
22.                ****  *         ***************   *** ***  *
23.                  ******         *************    **   **  *
24.                  ********        *************    *  ** ***
25.                    ********         ********          * *** ****
26.                    *********         ******  *        **** ** * **
27.                    *********         ****** * *           *** *   *
28.                      ******          ***** **             *****   *
29.                      *****            **** *            ********
30.                     *****             ****              *********
31.                     ****              **                 *******   *
32.                     ***                                       *    *
33.                     **     *                    *
34. ...................................................................."""
print("Nhập vào kí tự bạn muốn thay thế!")
messenge = input("> ")
for line in bitmap.splitlines():
    for kitu in line:
        for so,i in enumerate(kitu):
            if i ==" ":
                print(" ", end=" ")
            else:
                print(messenge[so%len(messenge)], end=" ")
    print()