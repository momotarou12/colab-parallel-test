# colab-parallel-test

# Python Parallel Performance Experiment

This repository contains Python code to experiment with the performance of parallel processing using `concurrent.futures.ThreadPoolExecutor`. It helps visualize how increasing the number of parallel workers affects the execution time of I/O-bound tasks (simulated here).
<img width="996" height="547" alt="result" src="https://github.com/user-attachments/assets/4bcf75f4-faab-4f98-a167-4b5325167cab" />

# Analysis of Duration Change
Execution time change becomes less than 1.0% per worker increase around MAX_WORKERS = 35
|index|MAX\_WORKERS|Duration \(seconds\)|Duration\_Change|Duration\_Change\_Percent|
|---|---|---|---|---|
|0|1|37\.52912402153015|NaN|NaN|
|1|2|19\.229813814163208|18\.299310207366943|48\.76029133232308|
|2|3|12\.548284530639648|6\.68152928352356|34\.745678497430156|
|3|4|9\.3532075881958|3\.1950769424438477|25\.4622608743235|
|4|5|7\.527191877365112|1\.8260157108306885|19\.52288232258641|
|5|6|6\.556263208389282|0\.9709286689758301|12\.898949366436277|
|6|7|5\.302881717681885|1\.2533814907073975|19\.11731501419272|
|7|8|4\.684385061264038|0\.6184966564178467|11\.663406603159498|
|8|9|4\.219585418701172|0\.4647996425628662|9\.922319290238798|
|9|10|3\.81242036819458|0\.4071650505065918|9\.649408889841151|
|10|11|3\.3622026443481445|0\.45021772384643555|11\.809236137819761|
|11|12|3\.1874639987945557|0\.17473864555358887|5\.197147942505017|
|12|13|2\.983635187149048|0\.2038288116455078|6\.394701609887747|
|13|14|2\.7192211151123047|0\.26441407203674316|8\.862144848526158|
|14|15|2\.508986473083496|0\.2102346420288086|7\.731428711714966|
|15|16|2\.447643756866455|0\.061342716217041016|2\.4449201649800845|
|16|17|2\.300180435180664|0\.14746332168579102|6\.024705240380972|
|17|18|2\.2159616947174072|0\.08421874046325684|3\.6613971310751543|
|18|19|2\.053514242172241|0\.16244745254516602|7\.330787934305078|
|19|20|2\.0024917125701904|0\.05102252960205078|2\.4846445451519394|
|20|21|1\.938917636871338|0\.06357407569885254|3\.1747485045646187|
|21|22|1\.8160831928253174|0\.12283444404602051|6\.335206906685718|
|22|23|1\.6988999843597412|0\.11718320846557617|6\.45252425266223|
|23|24|1\.6605074405670166|0\.03839254379272461|2\.259847203847817|
|24|25|1\.5899171829223633|0\.07059025764465332|4\.251125645094896|
|25|26|1\.5111758708953857|0\.07874131202697754|4\.952541734422058|
|26|27|1\.5351598262786865|0\.02398395538330078|1\.5871055014324749|
|27|28|1\.4303226470947266|0\.10483717918395996|6\.829072607905013|
|28|29|1\.4120562076568604|0\.01826643943786621|1\.2770852419185998|
|29|30|1\.3128435611724854|0\.099212646484375|7\.026111704788764|
|30|31|1\.3721728324890137|0\.05932927131652832|4\.519142498862701|
|31|32|1\.2535855770111084|0\.11858725547790527|8\.642297287200863|
|32|33|1\.3107550144195557|0\.057169437408447266|4\.5604734496670645|
|33|34|1\.192690134048462|0\.11806488037109375|9\.007394903873525|
|34|35|1\.1807670593261719|0\.011923074722290039|0\.999679160740469|
|35|36|1\.1443889141082764|0\.03637814521789551|3\.080890928533814|
|36|37|1\.1291203498840332|0\.015268564224243164|1\.3342111266553678|
|37|38|1\.0857417583465576|0\.043378591537475586|3\.8418040682670194|
|38|39|1\.0689027309417725|0\.016839027404785156|1\.550923806267596|
|39|40|1\.003067970275879|0\.06583476066589355|6\.159097433298619|
|40|41|0\.9919474124908447|0\.01112055778503418|1\.1086544595752206|
|41|42|1\.0328688621520996|0\.04092144966125488|4\.125364827405361|
|42|43|0\.9258520603179932|0\.10701680183410645|10\.361121896067695|
|43|44|0\.9932661056518555|0\.0674140453338623|7\.281297760541601|
|44|45|0\.9335088729858398|0\.059757232666015625|6\.016235963956352|
|45|46|0\.9203610420227051|0\.013147830963134766|1\.4084312794029759|
|46|47|0\.9152028560638428|0\.005158185958862305|0\.5604524445674063|
|47|48|0\.901613712310791|0\.013589143753051758|1\.4848231365335474|
|48|49|0\.9052553176879883|0\.0036416053771972656|0\.403898623931086|
|49|50|0\.870966911315918|0\.03428840637207031|3\.7877056010720276|
|50|51|0\.8498916625976562|0\.02107524871826172|2\.419753086419753|
|51|52|0\.8450217247009277|0\.004869937896728516|0\.5730069032379688|
|52|53|0\.8517742156982422|0\.006752490997314453|0\.799090816239584|
|53|54|0\.7724268436431885|0\.07934737205505371|9\.315540502715109|
|54|55|0\.7867414951324463|0\.014314651489257812|1\.8532048189498527|
|55|56|0\.8050854206085205|0\.01834392547607422|2\.3316331462834636|
|56|57|0\.750697135925293|0\.05438828468322754|6\.755591803180137|
|57|58|0\.7567451000213623|0\.006047964096069336|0\.8056463527884314|
|58|59|0\.7435719966888428|0\.013173103332519531|1\.740758325643293|
|59|60|0\.746711015701294|0\.003139019012451172|0\.4221540115051878|
|60|61|0\.710782527923584|0\.03592848777770996|4\.811565253790551|
|61|62|0\.7223496437072754|0\.011567115783691406|1\.6273776196331862|
|62|63|0\.7369773387908936|0\.014627695083618164|2\.0250158923793813|
|63|64|0\.6917850971221924|0\.04519224166870117|6\.132107364772556|
|64|65|0\.6797363758087158|0\.012048721313476562|1\.7416855846705752|
|65|66|0\.6573340892791748|0\.022402286529541016|3\.295731599311264|
|66|67|0\.6975090503692627|0\.04017496109008789|6\.111802467774538|
|67|68|0\.6899688243865967|0\.007540225982666016|1\.0810219564426018|
|68|69|0\.6739451885223389|0\.016023635864257812|2\.322370996762544|
|69|70|0\.6924731731414795|0\.018527984619140625|2\.7491827131764572|
|70|71|0\.6610181331634521|0\.031455039978027344|4\.542420009619744|
|71|72|0\.6303412914276123|0\.030676841735839844|4\.640847231985735|
|72|73|0\.633852481842041|0\.003511190414428711|0\.5570300505741075|
|73|74|0\.6189851760864258|0\.014867305755615234|2\.3455466660648394|
|74|75|0\.6464643478393555|0\.027479171752929688|4\.439390928013583|
|75|76|0\.6155858039855957|0\.030878543853759766|4\.776526958828207|
|76|77|0\.6020870208740234|0\.013498783111572266|2\.192835348732007|
|77|78|0\.5920250415802002|0\.010061979293823242|1\.671183557356328|
|78|79|0\.6270849704742432|0\.03505992889404297|5\.922034784282597|
|79|80|0\.598675012588501|0\.028409957885742188|4\.53047979514749|
|80|81|0\.5831265449523926|0\.015548467636108398|2\.5971465835664715|
|81|82|0\.5812029838562012|0\.0019235610961914062|0\.3298702679275986|
|82|83|0\.5650918483734131|0\.016111135482788086|2\.772032479236933|
|83|84|0\.5804643630981445|0\.015372514724731445|2\.7203568356153807|
|84|85|0\.5644247531890869|0\.016039609909057617|2\.7632376643156045|
|85|86|0\.5831658840179443|0\.018741130828857422|3\.3203949194232076|
|86|87|0\.5755763053894043|0\.007589578628540039|1\.301444209364364|
|87|88|0\.5396010875701904|0\.03597521781921387|6\.2502951359116405|
|88|89|0\.5463228225708008|0\.0067217350006103516|1\.2456859623612229|
|89|90|0\.5377926826477051|0\.008530139923095703|1\.5613735269114148|
|90|91|0\.5495991706848145|0\.011806488037109375|2\.195360483333969|
|91|92|0\.5377192497253418|0\.011879920959472656|2\.16156093261021|
|92|93|0\.528264045715332|0\.009455204010009766|1\.758390463952951|
|93|94|0\.5292370319366455|0\.0009729862213134766|0\.1841855846910683|
|94|95|0\.5390093326568604|0\.009772300720214844|1\.8464884598976206|
|95|96|0\.5183618068695068|0\.020647525787353516|3\.830643466891133|
|96|97|0\.5232429504394531|0\.004881143569946289|0\.9416479966810278|
|97|98|0\.5143506526947021|0\.008892297744750977|1\.6994586811504393|
|98|99|0\.516057014465332|0\.0017063617706298828|0\.3317506766425181|
|99|100|0\.48934388160705566|0\.026713132858276367|5\.176391776391776|

# Result

Testing with MAX_WORKERS = 1...
Finished in 37.5291 seconds.

Testing with MAX_WORKERS = 2...
Finished in 19.2298 seconds.

Testing with MAX_WORKERS = 3...
Finished in 12.5483 seconds.

Testing with MAX_WORKERS = 4...
Finished in 9.3532 seconds.

Testing with MAX_WORKERS = 5...
Finished in 7.5272 seconds.

Testing with MAX_WORKERS = 6...
Finished in 6.5563 seconds.

Testing with MAX_WORKERS = 7...
Finished in 5.3029 seconds.

Testing with MAX_WORKERS = 8...
Finished in 4.6844 seconds.

Testing with MAX_WORKERS = 9...
Finished in 4.2196 seconds.

Testing with MAX_WORKERS = 10...
Finished in 3.8124 seconds.

Testing with MAX_WORKERS = 11...
Finished in 3.3622 seconds.

Testing with MAX_WORKERS = 12...
Finished in 3.1875 seconds.

Testing with MAX_WORKERS = 13...
Finished in 2.9836 seconds.

Testing with MAX_WORKERS = 14...
Finished in 2.7192 seconds.

Testing with MAX_WORKERS = 15...
Finished in 2.5090 seconds.

Testing with MAX_WORKERS = 16...
Finished in 2.4476 seconds.

Testing with MAX_WORKERS = 17...
Finished in 2.3002 seconds.

Testing with MAX_WORKERS = 18...
Finished in 2.2160 seconds.

Testing with MAX_WORKERS = 19...
Finished in 2.0535 seconds.

Testing with MAX_WORKERS = 20...
Finished in 2.0025 seconds.

Testing with MAX_WORKERS = 21...
Finished in 1.9389 seconds.

Testing with MAX_WORKERS = 22...
Finished in 1.8161 seconds.

Testing with MAX_WORKERS = 23...
Finished in 1.6989 seconds.

Testing with MAX_WORKERS = 24...
Finished in 1.6605 seconds.

Testing with MAX_WORKERS = 25...
Finished in 1.5899 seconds.

Testing with MAX_WORKERS = 26...
Finished in 1.5112 seconds.

Testing with MAX_WORKERS = 27...
Finished in 1.5352 seconds.

Testing with MAX_WORKERS = 28...
Finished in 1.4303 seconds.

Testing with MAX_WORKERS = 29...
Finished in 1.4121 seconds.

Testing with MAX_WORKERS = 30...
Finished in 1.3128 seconds.

Testing with MAX_WORKERS = 31...
Finished in 1.3722 seconds.

Testing with MAX_WORKERS = 32...
Finished in 1.2536 seconds.

Testing with MAX_WORKERS = 33...
Finished in 1.3108 seconds.

Testing with MAX_WORKERS = 34...
Finished in 1.1927 seconds.

Testing with MAX_WORKERS = 35...
Finished in 1.1808 seconds.

Testing with MAX_WORKERS = 36...
Finished in 1.1444 seconds.

Testing with MAX_WORKERS = 37...
Finished in 1.1291 seconds.

Testing with MAX_WORKERS = 38...
Finished in 1.0857 seconds.

Testing with MAX_WORKERS = 39...
Finished in 1.0689 seconds.

Testing with MAX_WORKERS = 40...
Finished in 1.0031 seconds.

Testing with MAX_WORKERS = 41...
Finished in 0.9919 seconds.

Testing with MAX_WORKERS = 42...
Finished in 1.0329 seconds.

Testing with MAX_WORKERS = 43...
Finished in 0.9259 seconds.

Testing with MAX_WORKERS = 44...
Finished in 0.9933 seconds.

Testing with MAX_WORKERS = 45...
Finished in 0.9335 seconds.

Testing with MAX_WORKERS = 46...
Finished in 0.9204 seconds.

Testing with MAX_WORKERS = 47...
Finished in 0.9152 seconds.

Testing with MAX_WORKERS = 48...
Finished in 0.9016 seconds.

Testing with MAX_WORKERS = 49...
Finished in 0.9053 seconds.

Testing with MAX_WORKERS = 50...
Finished in 0.8710 seconds.

Testing with MAX_WORKERS = 51...
Finished in 0.8499 seconds.

Testing with MAX_WORKERS = 52...
Finished in 0.8450 seconds.

Testing with MAX_WORKERS = 53...
Finished in 0.8518 seconds.

Testing with MAX_WORKERS = 54...
Finished in 0.7724 seconds.

Testing with MAX_WORKERS = 55...
Finished in 0.7867 seconds.

Testing with MAX_WORKERS = 56...
Finished in 0.8051 seconds.

Testing with MAX_WORKERS = 57...
Finished in 0.7507 seconds.

Testing with MAX_WORKERS = 58...
Finished in 0.7567 seconds.

Testing with MAX_WORKERS = 59...
Finished in 0.7436 seconds.

Testing with MAX_WORKERS = 60...
Finished in 0.7467 seconds.

Testing with MAX_WORKERS = 61...
Finished in 0.7108 seconds.

Testing with MAX_WORKERS = 62...
Finished in 0.7223 seconds.

Testing with MAX_WORKERS = 63...
Finished in 0.7370 seconds.

Testing with MAX_WORKERS = 64...
Finished in 0.6918 seconds.

Testing with MAX_WORKERS = 65...
Finished in 0.6797 seconds.

Testing with MAX_WORKERS = 66...
Finished in 0.6573 seconds.

Testing with MAX_WORKERS = 67...
Finished in 0.6975 seconds.

Testing with MAX_WORKERS = 68...
Finished in 0.6900 seconds.

Testing with MAX_WORKERS = 69...
Finished in 0.6739 seconds.

Testing with MAX_WORKERS = 70...
Finished in 0.6925 seconds.

Testing with MAX_WORKERS = 71...
Finished in 0.6610 seconds.

Testing with MAX_WORKERS = 72...
Finished in 0.6303 seconds.

Testing with MAX_WORKERS = 73...
Finished in 0.6339 seconds.

Testing with MAX_WORKERS = 74...
Finished in 0.6190 seconds.

Testing with MAX_WORKERS = 75...
Finished in 0.6465 seconds.

Testing with MAX_WORKERS = 76...
Finished in 0.6156 seconds.

Testing with MAX_WORKERS = 77...
Finished in 0.6021 seconds.

Testing with MAX_WORKERS = 78...
Finished in 0.5920 seconds.

Testing with MAX_WORKERS = 79...
Finished in 0.6271 seconds.

Testing with MAX_WORKERS = 80...
Finished in 0.5987 seconds.

Testing with MAX_WORKERS = 81...
Finished in 0.5831 seconds.

Testing with MAX_WORKERS = 82...
Finished in 0.5812 seconds.

Testing with MAX_WORKERS = 83...
Finished in 0.5651 seconds.

Testing with MAX_WORKERS = 84...
Finished in 0.5805 seconds.

Testing with MAX_WORKERS = 85...
Finished in 0.5644 seconds.

Testing with MAX_WORKERS = 86...
Finished in 0.5832 seconds.

Testing with MAX_WORKERS = 87...
Finished in 0.5756 seconds.

Testing with MAX_WORKERS = 88...
Finished in 0.5396 seconds.

Testing with MAX_WORKERS = 89...
Finished in 0.5463 seconds.

Testing with MAX_WORKERS = 90...
Finished in 0.5378 seconds.

Testing with MAX_WORKERS = 91...
Finished in 0.5496 seconds.

Testing with MAX_WORKERS = 92...
Finished in 0.5377 seconds.

Testing with MAX_WORKERS = 93...
Finished in 0.5283 seconds.

Testing with MAX_WORKERS = 94...
Finished in 0.5292 seconds.

Testing with MAX_WORKERS = 95...
Finished in 0.5390 seconds.

Testing with MAX_WORKERS = 96...
Finished in 0.5184 seconds.

Testing with MAX_WORKERS = 97...
Finished in 0.5232 seconds.

Testing with MAX_WORKERS = 98...
Finished in 0.5144 seconds.

Testing with MAX_WORKERS = 99...
Finished in 0.5161 seconds.

Testing with MAX_WORKERS = 100...
Finished in 0.4893 seconds.

--- Experiment Summary ---
    MAX_WORKERS  Duration (seconds)
0             1           37.529124
1             2           19.229814
2             3           12.548285
3             4            9.353208
4             5            7.527192
..          ...                 ...
95           96            0.518362
96           97            0.523243
97           98            0.514351
98           99            0.516057
99          100            0.489344

[100 rows x 2 columns]


## Files

-   `parallel_experiment.py` (or similar): The main Python script containing the parallel execution experiment logic.
-   (Optional) `plot_results.ipynb` or add plotting code within the main script: Code to visualize the experiment results.

## Setup

No external dependencies beyond standard Python libraries (`time`, `concurrent.futures`, `random`, `pandas`, `matplotlib`, `seaborn`) are strictly required if you run this in an environment like Google Colab or a standard Python installation with these libraries.

## How to Run the Experiment

1.  Save the provided experiment code into a Python file (e.g., `parallel_experiment.py`).
2.  Run the script from your terminal:
    ```bash
    python parallel_experiment.py
    ```
    Or, if using a Jupyter Notebook/Google Colab, paste and run the code cells.

The script will test a range of `MAX_WORKERS` values and print a summary table of execution times.

## How to Visualize Results

If you have the plotting code (either in the same script or a separate notebook), run it after the experiment completes. It will generate a line plot showing Execution Time vs. Number of Parallel Workers.

## Code Description

-   `classify_tag(tag)`: A mock function simulating a task with latency (like an API call).
-   `parallel_classify(tags, max_workers)`: Executes the mock task in parallel using `ThreadPoolExecutor` and measures the duration.
-   The main part of the script loops through `worker_counts_to_test`, runs the `parallel_classify` for each, and collects results.
-   The plotting code uses `matplotlib` and `seaborn` to create a line graph from the collected results (`summary_df`).

## Customization

-   You can change the size of the dummy data (`tags_to_classify_test`).
-   Modify `worker_counts_to_test` to test a different range or granularity of worker counts.
-   Adjust the `time.sleep()` duration in `classify_tag` to simulate different task latencies.

## License

[Specify your license here, e.g., MIT License]
