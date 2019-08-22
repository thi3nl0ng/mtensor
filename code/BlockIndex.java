package mzoom;
import com.google.common.collect.Ordering;
import com.google.common.primitives.Doubles;
import com.google.common.primitives.Ints;

import java.io.Serializable;
import java.util.ArrayList;
import java.util.Arrays;
import java.util.Comparator;
import java.util.List;


    // Ordering Class also implements Comparator Interface
   
public class BlockIndex {
	  public int index ;
	  public double density; 
	  public BlockIndex(int i, double d)
	  {
		  index = i;
		  density = d;
	  }
	  
	  public static Ordering<BlockIndex> ORDERING_BY_Density = new Ordering<BlockIndex>(){
	        public int compare(BlockIndex a, BlockIndex b) {
	            return Doubles.compare(a.density, b.density);
	        }
	    };
  	
	  	public static void main(String[] args)
	  	{
	  		Ordering<BlockIndex> order = Ordering.from(ORDERING_BY_Density);
	  		List<BlockIndex> blockList = new ArrayList<BlockIndex>();
	  		for (int i = 0; i < 10; i++) {  
	  			BlockIndex a = new BlockIndex(i, i);
	  			blockList.add(a);
	  		}
	  		List<BlockIndex> topk = order.greatestOf(blockList, 4);
	  		System.out.println(topk);
	  	}
	}

   