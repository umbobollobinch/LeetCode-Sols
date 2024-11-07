public class Solution {
    public int RomanToInt(string s) {
        int num = 0;
        string tmpstr = s;
        int arraySize;
        Dictionary<string, int> romanDict = new Dictionary<string, int> {{"M",1000},{"D",500},{"C",100},{"L",50},{"X",10},{"V",5},{"I",1}};
        
        foreach(KeyValuePair<string, int> dictItem in romanDict){
            string[] tmparr = tmpstr.Split(dictItem.Key);
            arraySize = tmparr.Length;
            for(int i = 0; i < arraySize - 1; i++){
                if (tmparr[i] == ""){
                    num = num + dictItem.Value;
                }else{
                    num = num + dictItem.Value - romanDict[tmparr[i]];
                }
            }
            tmpstr = tmparr[arraySize - 1];
            //Console.WriteLine(arraySize);
            //Console.WriteLine(tmparr[arraySize - 1]);
            //Console.WriteLine(string.Join(",", tmparr));
        }
        
        return num;
    }
}
