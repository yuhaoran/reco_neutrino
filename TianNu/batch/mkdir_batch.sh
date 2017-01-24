#export OUTPUT_PATH='/WORK/bnu_ztj_1/yuanshuo/tildes/LOS29-3dm/'
export OUTPUT_PATH='/WORK/bnu_ztj_1/yuanshuo/tildes/analysis/'

#'/HOME/bnu_ztj_1/WORKSPACE/tides/LOS3/'

let irank=0
let nrank=13823

while [ $irank -le $nrank ]; do

   ##echo $irank

   dirname=$OUTPUT_PATH'node'$irank
   mkdir -vp $dirname
   let irank=$irank+1
done
