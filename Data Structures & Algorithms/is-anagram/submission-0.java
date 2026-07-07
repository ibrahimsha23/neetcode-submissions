class Solution {
    public boolean isAnagram(String s, String t) {
        if(s.length() != t.length()){
            return false;
        }

        int [] dataHolder = new int [26];

        java.util.Arrays.fill(dataHolder, 0);
        char ch = 'a';
        int ordinal = (int) ch;

        for (char i : s.toCharArray()){
            dataHolder[(int) i - ordinal] += 1;

        }

        for (char k : t.toCharArray()){
            dataHolder[(int)k  - ordinal] -= 1;

        }

        for (int l: dataHolder){
            
            if(l!= 0){
                return false;
            }
        }

        return true;
        


    }
}
