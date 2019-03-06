var s1option=[{'python1': 'python1', 'python2': 'python2', 'python3': 'python3', 'python4': 'python4'}];
var s2option=[{'python1': [{'python1-未知1': '未知1'}, {'python1-未知2': '未知2'}], 'python2': [{'python2-未知1': '未知1'}, {'python2-未知2': '未知2'}], 'python3': [{'python3-未知1': '未知1'}, {'python3-未知2': '未知2'}], 'python4': [{'python4-未知1': '未知1'}, {'python4-未知2': '未知2'}]}];
var s3option=[{'python1-未知1': [{'python1-未知1-PolynomialFeaturesTransformer': 'PolynomialFeaturesTransformer'}, {'python1-未知1-未知': '未知'}], 'python1-未知2': [{'python1-未知2-B1': 'B1'}, {'python1-未知2-B2': 'B2'}], 'python2-未知1': [{'python2-未知1-PairwiseSampleTransformer': 'PairwiseSampleTransformer'}, {'python2-未知1-未知': '未知'}], 'python2-未知2': [{'python2-未知2-B1': 'B1'}, {'python2-未知2-B2': 'B2'}], 'python3-未知1': [{'python3-未知1-MaxMinScalar': 'MaxMinScalar'}, {'python3-未知1-未知': '未知'}], 'python3-未知2': [{'python3-未知2-B1': 'B1'}, {'python3-未知2-B2': 'B2'}], 'python4-未知1': [{'python4-未知1-SklearnPairwiseL2REstimator': 'SklearnPairwiseL2REstimator'}, {'python4-未知1-未知': '未知'}], 'python4-未知2': [{'python4-未知2-B1': 'B1'}, {'python4-未知2-B2': 'B2'}]}];
var s4option=[{'python1-未知1-PolynomialFeaturesTransformer': [{'python1-未知1-PolynomialFeaturesTransformer-degree': 'degree'}, {'python1-未知1-PolynomialFeaturesTransformer-interaction_only': 'interaction_only'}, {'python1-未知1-PolynomialFeaturesTransformer-first_degree': 'first_degree'}], 'python1-未知1-未知': [{'python1-未知1-未知-C1': 'C1'}, {'python1-未知1-未知-C2': 'C2'}], 'python1-未知2-B1': [{'python1-未知2-B1-C1': 'C1'}, {'python1-未知2-B1-C2': 'C2'}], 'python1-未知2-B2': [{'python1-未知2-B2-C1': 'C1'}, {'python1-未知2-B2-C2': 'C2'}], 'python2-未知1-PairwiseSampleTransformer': [{'python2-未知1-PairwiseSampleTransformer-空': '空'}], 'python2-未知1-未知': [{'python2-未知1-未知-C1': 'C1'}, {'python2-未知1-未知-C2': 'C2'}], 'python2-未知2-B1': [{'python2-未知2-B1-C1': 'C1'}, {'python2-未知2-B1-C2': 'C2'}], 'python2-未知2-B2': [{'python2-未知2-B2-C1': 'C1'}, {'python2-未知2-B2-C2': 'C2'}], 'python3-未知1-MaxMinScalar': [{'python3-未知1-MaxMinScalar-feature_range': 'feature_range'}], 'python3-未知1-未知': [{'python3-未知1-未知-C1': 'C1'}, {'python3-未知1-未知-C2': 'C2'}], 'python3-未知2-B1': [{'python3-未知2-B1-C1': 'C1'}, {'python3-未知2-B1-C2': 'C2'}], 'python3-未知2-B2': [{'python3-未知2-B2-C1': 'C1'}, {'python3-未知2-B2-C2': 'C2'}], 'python4-未知1-SklearnPairwiseL2REstimator': [{'python4-未知1-SklearnPairwiseL2REstimator-train_sample_percentage': 'train_sample_percentage'}, {'python4-未知1-SklearnPairwiseL2REstimator-interaction_only': 'interaction_only'}, {'python4-未知1-SklearnPairwiseL2REstimator-enable_grid_search_cv': 'enable_grid_search_cv'}, {'python4-未知1-SklearnPairwiseL2REstimator-grid_search_param': 'grid_search_param'}], 'python4-未知1-未知': [{'python4-未知1-未知-C1': 'C1'}, {'python4-未知1-未知-C2': 'C2'}], 'python4-未知2-B1': [{'python4-未知2-B1-C1': 'C1'}, {'python4-未知2-B1-C2': 'C2'}], 'python4-未知2-B2': [{'python4-未知2-B2-C1': 'C1'}, {'python4-未知2-B2-C2': 'C2'}]}];


// var四级选择  目标从json中调取  那么 还有可能从数据库调取  

    //addEventListener() 方法 为 <button> 元素添加点击事件
    document.addEventListener('DOMContentLoaded',function(){
      
	  //innerHTML 属性设置或返回表格行的开始和结束标签之间的 HTML。
	  //document.querySelector("#demo") 获取文档中 id="demo" 的元素  
      document.querySelector('#s1').innerHTML='<option disabled selected value="">----</option>';
	  document.querySelector('#s2').innerHTML='<option disabled selected value="">----</option>';
	  document.querySelector('#s3').innerHTML='<option disabled selected value="">----</option>';
	  
      document.querySelector('#s5').innerHTML='<option disabled selected value="">----</option>';
      document.querySelector('#s6').innerHTML='<option disabled selected value="">----</option>';
      document.querySelector('#s7').innerHTML='<option disabled selected value="">----</option>'; 

      document.querySelector('#s9').innerHTML='<option disabled selected value="">----</option>';
      document.querySelector('#s10').innerHTML='<option disabled selected value="">----</option>';
      document.querySelector('#s11').innerHTML='<option disabled selected value="">----</option>'; 
	  
      document.querySelector('#s13').innerHTML='<option disabled selected value="">----</option>';
      document.querySelector('#s14').innerHTML='<option disabled selected value="">----</option>';
      document.querySelector('#s15').innerHTML='<option disabled selected value="">----</option>'; 	  
      //selected属性 有预选  选择？
      //那也就是每个的第四个没变   怎么动态的增加？提前设置好？
	  //其实就是抓取对应的ID把提前预留的字符显示出来

      
      // 四级选择联动 写四级选择联动 由几个function组成  写的是第一级 
      // 加载第一级下拉列表 设load_select1函数 由s调用 参数为具体选择的ID
    function load_select1(s){
        s_select=document.querySelector(s);   //用document.querySelector(s) 抓取所求id 由s_select表示
        option_html='<option disabled selected value="">---</option>'; //option_html获取 html的option
		//同时现在所求的ID在页面显示的还是 字符‘选择’
                      
                
                // ???????key应该是前边我所选的  key怎么获取的
			    //一个for循环 i循环第一级选择找对应的显示 循环次数肯定不能超过列表本身的长度
               for(var i=0;i<s1option.length;i++){  //设变量i i小于一级选项字典长度  i++                   
                   for(var key in s1option[i]){ //再次for循环 设变量key  循环一级选项 获取该选项名做key
                       option_html+='<option value="'+key+'">'+s1option[i][key]+'</option>'; //??????为什么不是= 而是+=
                   }   //将获取到的i 和 key 获取一级字典的值
               }
          s_select.innerHTML=option_html; //获取选项  将当前选的选项渲染成所选的字符显示
     };
      

      load_select1('#s1'); //第一级选择 1 5 9 调用前边定义的函数
      load_select1('#s5');
      load_select1('#s9');
      load_select1('#s13');


    //1级的已经处理完 按照所选的选项显示出来了 开始
    // 加载2,3,4级下拉列表
    // 设新的函数       
    function load_select2(s_1,s_2,s_3,s_4,options){ //新函数参数 由上一个参数加载确定下一个参数前段渲染的字符 同时需要参数字典

		//querySelectorAll() 返回匹配的元素的集合，如果没有返回的就是一个空的nodelist  获取取的值是什么
		//forEach 列出数组的每个元素：
		//回调方法 当做参数传入后 会在相应的事件触发后调用
        document.querySelectorAll(s_1).forEach(function(option){ //获取第一个参数
		//表示只会执行 function , 但是不会传回 function 中之回传值
		//被选择时触发函数  所选的值代入函数
         option.onclick=function(){ //被选择时触发函数

         s_select=document.querySelector(s_2);  //格式获取  获取s_2的id 并接下来对其进行渲染
		 //渲染内容为 load_option函数对两个参数代入进去所处理的结果
         s_select.innerHTML=load_option(option.value,options); //加载下拉列表函数
		 //相当于根据你传入的第一个参数的选择  然后带入处理函数 获得第二个参数页面所渲染的内容

		 //innerHTML 属性设置或返回表格行的开始和结束标签之间的 HTML。
         document.querySelector(s_3).innerHTML=''; //这个怎么没有了
         document.querySelector(s_4).innerHTML='';
         return false;}; // return false，事件处理函数会取消事件，不再继续向下执行。比如表单将终止提交
       });
     };

      //全部调用
     load_select2('#s1','#s2','','',s2option);
     load_select2('#s5','#s6','','',s2option);
     load_select2('#s9','#s10','','',s2option);
     load_select2('#s13','#s14','','',s2option);

     load_select2('#s2','#s3','','',s3option);
     load_select2('#s6','#s7','','',s3option);
     load_select2('#s10','#s11','','',s3option);
     load_select2('#s14','#s15','','',s3option);

     load_select2('#s3','#s4','','',s4option);
     load_select2('#s7','#s8','','',s4option);
     load_select2('#s11','#s12','','',s4option);
     load_select2('#s15','#s16','','',s4option);
 

    // 加载下拉列表函数   获取下一个参数的值所调取的id
    function load_option(lastselect,soption) {   //lastselect 后一个选择？ 给的是所选参数的value  soption 查询的字典
          option_html='' //自己新设一个 从新开始写
          for(var i=0;i<soption.length;i++){ //设一个i  i为循环的次数 是字典的长度  不能超字典的长度         
           for(k in soption[i]){ //循环字典里的每一个ID
            if(k==lastselect){  //如果找到与key相同的ID 开始处理
              
              s=soption[i][k] //获取到其具体的值 放入s中
              for(var j=0;j<s.length;j++){  //
                for(k2 in s[j]){  //现在是三级判断   前三级用这个处理
                option_html+='<option value="'+k2+'">'+s[j][k2]+'</option>';
              };
              };
            };  //形成新的option_html 并返回
           };
         };
         return option_html;
        };
     


       // 生成第四级选项框
     //新写函数   三个参数  s 选择块id ,selection_list 前端div的id , y 不知道干什么的
    function load_inputlist(s,selection_list,y){

    //获取所选参数的集合  这次确实会是多个
    //forEach 列出数组的每个元素：
    document.querySelectorAll(s).forEach(function(option){
                option.onchange=function(){  //事件发生时，执行一段js代码
                    select_input(option.value,selection_list,y);    //select_input  执行输入框和解释  
					//y是因为select_input函数需要这个参数  所以之前的就传进来了
                    return false;  //什么时候加这样的话
                };
         });

       };
        //4 8 12 单独处理
       load_inputlist('#s4','#selection_list1','I');
       load_inputlist('#s8','#selection_list2','II');
       load_inputlist('#s12','#selection_list3','III');
       load_inputlist('#s16','#selection_list4','IIII');
     


    // 加载excel解释
    function load_explanation(option_value,idname){           
        const request = new XMLHttpRequest();        
        request.open('GET','/'+option_value+'/');
        request.onload=()=>{
            const response=request.responseText;
            const data=JSON.parse(response);
            console.log([data[0]])
            const explaination=document.createElement('p');
            explaination.innerHTML=data[0].content;
            document.querySelector('#'+idname+'').append(explaination);
            };
            request.send();
        };


   // 生成输入框及解释
   //select_input 生成输入框和解释的函数 被第4级下拉框所调用
   //三个参数option_value 传入的就是所选参数的value      ,selection_list 前段的哪个div的id   ,y I II III
    function select_input(option_value,selection_list,y){

      idname=''+y+'-'+option_value+''; //生成加载解释所需的参数  I y加上选项的标识符  I-id

    	if(document.querySelector('#'+idname+'')){ //如果选的选项 这个if什么意思  什么也没做啊
 
    	}
    	else{        
    		// 生成输入框的div
            const select=document.createElement('div');
            select.className='selection'
            document.querySelector(selection_list).append(select);

            //  创建解释的div             
            const explain=document.createElement('div');
            explain.id=idname;

            load_explanation(option_value,explain.id);  //加载excel解释
            select.append(explain);

            // 可以删除选择框
            const remove=document.createElement('button'); //创建一个按钮
            remove.className='remove';
            remove.innerHTML='x';
            select.append(remove);

            //当点击按钮的时候删除输入框
            remove.onclick=function(){
                this.parentElement.remove()
            }

            // 创建输入信息的div
            const s_input=document.createElement('div');
            s_input.className='s_input';
            s_input.innerHTML='<input type="text" name="'+idname+'"><br><br>';            
            select.append(s_input);

    	};
            }


 });
