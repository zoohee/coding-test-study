package PGS.Lv1;
import java.util.*;

public class 같은_숫자는_싫어 {
    public List<Integer> solution(int []arr) throws Exception {
        List<Integer> answer = new ArrayList<>();
        int tmp = arr[0];
        answer.add(tmp);
        for(int i=1; i<arr.length; i++) {
            if(tmp==arr[i]) continue;
            answer.add(arr[i]);
            tmp = arr[i];
        }
        return answer;
    }
}