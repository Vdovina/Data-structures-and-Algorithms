#### Сортировка слиянием ####


|                          |              |
|:------------------------:|:------------:|
| Имя входного файла:      | input.txt    |
| Имя выходного файла:     | output.txt   |
| Ограничение по времени:  | 2 секунды    |
| Ограничение по памяти:   | 256 мегабайт |

Дан массив целых чисел. Ваша задача — отсортировать его в порядке неубывания с помощью сортировки слиянием.

Чтобы убедиться, что Вы действительно используете сортировку слиянием, мы просим Вас, после каждого осуществленного слияния (то есть, когда соответствующий подмассив уже отсортирован!), выводить индексы граничных элементов и их значения.

Формат входного файла
В первой строке входного файла содержится число ![equation](http://latex.codecogs.com/svg.latex?\inline&space;n) (![equation](https://latex.codecogs.com/svg.latex?\inline&space;(1&space;\le&space;n&space;\le&space;10^5)) — число элементов в массиве. Во второй строке находятся n целых чисел, по модулю не превосходящих ![equation](http://latex.codecogs.com/svg.latex?\inline&space;10^9).

Формат выходного файла
Выходной файл состоит из нескольких строк.

В последней строке выходного файла требуется вывести отсортированный в порядке неубывания массив, данный на входе. Между любыми двумя числами должен стоять ровно один пробел.

Все предшествующие строки описывают осуществленные слияния, по одному на каждой строке. Каждая такая строка должна содержать по четыре числа: ![equation](https://latex.codecogs.com/svg.latex?\inline&space;I_f) ![equation](https://latex.codecogs.com/svg.latex?\inline&space;I_l) ![equation](https://latex.codecogs.com/svg.latex?\inline&space;V_f) ![equation](https://latex.codecogs.com/svg.latex?\inline&space;V_l), где ![equation](https://latex.codecogs.com/svg.latex?\inline&space;I_f) — индекс начала области слияния, ![equation](https://latex.codecogs.com/svg.latex?\inline&space;I_l) — индекс конца области слияния, ![equation](https://latex.codecogs.com/svg.latex?\inline&space;V_f) — значение первого элемента области слияния, ![equation](https://latex.codecogs.com/svg.latex?\inline&space;V_l) — значение последнего элемента области слияния.

Все индексы начинаются с единицы (то есть, ![equation](https://latex.codecogs.com/svg.latex?\inline&space;1&space;\le&space;I_f&space;\le&space;I_l&space;\le&space;n)). __Индексы области слияния должны описывать положение области слияния в исходном массиве!__ Допускается не выводить информацию о слиянии для подмассива длиной 1, так как он отсортирован по определению.

Приведем небольшой пример: отсортируем массив [9, 7, 5, 8]. Рекурсивная часть сортировки слиянием (процедура SORT(![equation](http://latex.codecogs.com/svg.latex?\inline&space;A), ![equation](http://latex.codecogs.com/svg.latex?\inline&space;L), ![equation](http://latex.codecogs.com/svg.latex?\inline&space;R)), где ![equation](http://latex.codecogs.com/svg.latex?\inline&space;A) — сортируемый массив, ![equation](http://latex.codecogs.com/svg.latex?\inline&space;L) — индекс начала области слияния, ![equation](http://latex.codecogs.com/svg.latex?\inline&space;R) — индекс конца области слияния) будет вызвана с ![equation](https://latex.codecogs.com/svg.latex?\inline&space;A&space;=&space;[9,&space;7,&space;5,&space;8]), ![equation](https://latex.codecogs.com/svg.latex?\inline&space;L&space;=&space;1), ![equation](https://latex.codecogs.com/svg.latex?\inline&space;R&space;=&space;4) и выполнит следующие действия:

* разделит область слияния ![equation](https://latex.codecogs.com/svg.latex?\inline&space;[1;&space;4]) на две части, ![equation](https://latex.codecogs.com/svg.latex?\inline&space;[1;&space;2]) и ![equation](https://latex.codecogs.com/svg.latex?\inline&space;[3;&space;4]);
* выполнит вызов SORT(![equation](http://latex.codecogs.com/svg.latex?\inline&space;A), ![equation](https://latex.codecogs.com/svg.latex?\inline&space;L&space;=&space;1), ![equation](https://latex.codecogs.com/svg.latex?\inline&space;R&space;=&space;2)):
    * разделит область слияния ![equation](https://latex.codecogs.com/svg.latex?\inline&space;[1;&space;2]) на две части, ![equation](https://latex.codecogs.com/svg.latex?\inline&space;[1;&space;1]) и ![equation](https://latex.codecogs.com/svg.latex?\inline&space;[2;&space;2]);
    * получившиеся части имеют единичный размер, рекурсивные вызовы можно не делать;
    * осуществит слияние, после чего ![equation](http://latex.codecogs.com/svg.latex?\inline&space;A) станет равным ![equation](https://latex.codecogs.com/svg.latex?\inline&space;[7,&space;9,&space;5,&space;8]);
    * выведет описание слияния: ![equation](https://latex.codecogs.com/svg.latex?\inline&space;I_f&space;=&space;L&space;=&space;1), ![equation](https://latex.codecogs.com/svg.latex?\inline&space;I_l&space;=&space;R&space;=&space;2),![equation](https://latex.codecogs.com/svg.latex?\inline&space;V_f&space;=&space;A_L&space;=&space;7), ![equation](https://latex.codecogs.com/svg.latex?\inline&space;V_l&space;=&space;A_R&space;=&space;9).
* выполнит вызов SORT(![equation](http://latex.codecogs.com/svg.latex?\inline&space;A), ![equation](https://latex.codecogs.com/svg.latex?\inline&space;L&space;=&space;3), ![equation](https://latex.codecogs.com/svg.latex?\inline&space;R&space;=&space;4)):
    * разделит область слияния ![equation](https://latex.codecogs.com/svg.latex?\inline&space;[3;&space;4]) на две части, ![equation](https://latex.codecogs.com/svg.latex?\inline&space;[3;&space;3]) и ![equation](https://latex.codecogs.com/svg.latex?\inline&space;[4;&space;4]);
    * получившиеся части имеют единичный размер, рекурсивные вызовы можно не делать;
    * осуществит слияние, после чего ![equation](http://latex.codecogs.com/svg.latex?\inline&space;A) станет равным ![equation](https://latex.codecogs.com/svg.latex?\inline&space;[7,&space;9,&space;5,&space;8]);
    * выведет описание слияния: ![equation](https://latex.codecogs.com/svg.latex?\inline&space;I_f&space;=&space;L&space;=&space;3), ![equation](https://latex.codecogs.com/svg.latex?\inline&space;I_l&space;=&space;R&space;=&space;4), ![equation](https://latex.codecogs.com/svg.latex?\inline&space;V_f&space;=&space;A_L&space;=&space;5), ![equation](https://latex.codecogs.com/svg.latex?\inline&space;V_l&space;=&space;A_R&space;=&space;8).
* осуществит слияние, после чего A станет равным ![equation](https://latex.codecogs.com/svg.latex?\inline&space;[5,&space;7,&space;8,&space;9]);
* выведет описание слияния: ![equation](https://latex.codecogs.com/svg.latex?\inline&space;I_f&space;=&space;L&space;=&space;1), ![equation](https://latex.codecogs.com/svg.latex?\inline&space;I_l&space;=&space;R&space;=&space;4), ![equation](https://latex.codecogs.com/svg.latex?\inline&space;V_f&space;=&space;A_L&space;=&space;5), ![equation](https://latex.codecogs.com/svg.latex?\inline&space;V_l&space;=&space;A_R&space;=&space;9).

Описания слияний могут идти в произвольном порядке, необязательно совпадающем с порядком их выполнения. Однако, с целью повышения производительности, рекомендуем выводить эти описания сразу, не храня их в памяти. Именно по этой причине отсортированный массив выводится в самом конце.

__Исключением из этого правила, возможно, является PyPy__ — по причине отсутствия буферизации вывода, при решения задачи на этом языке рекомендуется собрать все описания слияния в один буфер, а затем вывести его как одно целое. Обертка ввода-вывода для PyPy, расположенная [на GitHub](https://github.com/mbuzdalov/pads-io/blob/master/pypy/openedu_io.py)) и доступная (при компиляции решения в тестирующей системе) как модуль openedu_io, делает это автоматически.

Корректность выданного Вами сценария сортировки слиянием проверяется специальной программой. Любая корректная сортировка слиянием, делящая подмассивы на две части (необязательно равных!), будет зачтена, если успеет завершиться, уложившись в ограничения.

__Пример__

|      input.txt      |     output.txt      |
|:-------------------:|:-------------------:|
| 10                  | 1 2 1 8             |
| 1 8 2 1 4 7 3 2 3 6 | 3 4 1 2             |
|                     | 1 4 1 8             |
|                     | 5 6 4 7             |
|                     | 1 6 1 8             |
|                     | 7 8 2 3             | 
|                     | 9 10 3 6            |
|                     | 7 10 2 6            |
|                     | 1 10 1 8            |
|                     | 1 1 2 2 3 3 4 6 7 8 |

Результаты работы Вашего решения

|№ теста| Результат | Время, с |  Память  | Размер входного файла | Размер выходного файла |
|:------:|:---------:|:--------:|:--------:|:---------------------:|:----------------------:|
|  Max	 |           |	1.575	| 22925312 |	1039245            | 4403894                |
| 1	     | OK	     |  0.062	| 6520832  | 	25	               | 105                    |
| 2	     | OK	     |  0.062	| 6549504  |	6	               | 3                      |    
| 3	     | OK	     |  0.062	| 6541312  |	8	               | 14                     |
| 4	     | OK	     |  0.062	| 6512640  |	8	               | 14                     |    
| 5	     | OK	     |  0.062	| 6520832  |	42	               | 155                    |
| 6	     | OK	     |  0.046	| 6504448  |	43	               | 155                    |    
| 7	     | OK	     |  0.062	| 6512640  |	51	               | 179                    |
| 8	     | OK	     |  0.046	| 6569984  |	45	               | 161                    |
| 9	     | OK	     |  0.046	| 6508544  |	105	               | 332                    |
| 10	 | OK	     |  0.046	| 6516736  |	110	               | 343                    |
| 11	 | OK	     |  0.062	| 6524928  |	107	               | 336                    |
| 12	 | OK	     |  0.062	| 6488064  |	461	               | 2041                   |
| 13	 | OK	     |  0.078	| 6533120  |	560	               | 2332                   |
| 14	 | OK	     |  0.046	| 6549504  |	388	               | 1821                   |
| 15	 | OK	     |  0.078	| 6541312  |	408	               | 1879                   |
| 16	 | OK	     |  0.062	| 6545408  |	1042	           | 3776                   |
| 17	 | OK	     |  0.062	| 6520832  |	1043	           | 3786                   |
| 18	 | OK	     |  0.046	| 6524928  |	1044	           | 3781                   |
| 19	 | OK	     |  0.062	| 6688768  |	5587	           | 25512                  |
| 20	 | OK	     |  0.046	| 6746112  |	6733	           | 28934                  |
| 21	 | OK	     |  0.062	| 6627328  |	4737	           | 22958                  |
| 22	 | OK	     |  0.046	| 6676480  |	5685	           | 25796                  |
| 23	 | OK	     |  0.062	| 6680576  |	10383	           | 39970                  |
| 24	 | OK	     |  0.109	| 6742016  |	10421	           | 40066                  |
| 25	 | OK	     |  0.093	| 6762496  |	10420	           | 40049                  |
| 26	 | OK	     |  0.218	| 8093696  |	65880	           | 305381                 |
| 27	 | OK	     |  0.202	| 8159232  |	77550	           | 340370                 |
| 28	 | OK	     |  0.187	| 8134656  |	57488	           | 280210                 |
| 29	 | OK	     |  0.218	| 8077312  |	68090	           | 311997                 |
| 30	 | OK	     |  0.218	| 8347648  |	103872	           | 420234                 |
| 31	 | OK	     |  0.156	| 8445952  |	103940	           | 420401                 |
| 32	 | OK	     |  0.218	| 8335360  |	103842	           | 420155                 |
| 33	 | OK	     |  1.513	| 20393984 |    758839	           | 3554240                |
| 34	 | OK	     |  1.513	| 21319680 |	875802	           | 3905093                |
| 35	 | OK	     |  1.482	| 20152320 |	675241	           | 3303445                |
| 36	 | OK	     |  1.528	| 19947520 |	782803	           | 3626101                |
| 37	 | OK	     |  1.560	| 22118400 |	1038992	           | 4403366                |
| 38	 | OK	     |  1.575	| 22863872 |	1038702	           | 4402359                |
| 39	 | OK	     |  1.544	| 22925312 |	1039245	           | 4403894                |
    