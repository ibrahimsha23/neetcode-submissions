
class Solution {

    private String sortString(String data){
            char[] charArrays = data.toCharArray();
            java.util.Arrays.sort(charArrays);
            return new String(charArrays);
    }

    public List<List<String>> groupAnagrams(String[] strs) {


        java.util.Map<String, List<String>> anagrams = new HashMap();


        for (String strEle: strs){

            String sortedData = sortString(strEle);

            if(!anagrams.containsKey(sortedData)){
                anagrams.put(sortedData, new ArrayList<>());

            } 
            anagrams.get(sortedData).add(strEle);

        }

        return new ArrayList(anagrams.values());





        
    }
}
