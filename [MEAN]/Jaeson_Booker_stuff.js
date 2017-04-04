function runningLogger(){
  console.log('I is running');
}
function xBy10(val){
  val *= 10;
  console.log(val)
  return val;
}
xBy10(5);
function runningLogger3(){
  return('I is running');
}
function runningLogger2(){
  return('I is not running');
}
function myFunctionRunner(param){
  if (typeof(param)=='function'){
    param();
  }
}
function myDoubleConsoleLog(param1,param2){
  if (typeof(param1) == 'function' && typeof(param2) == 'function'){
    console.log(param1(), param2());
  }
}
function caller2(param){
  console.log('starting');
  var x = setTimeout(function(){
    if (typeof(param)=='function'){
      param(runningLogger3, runningLogger2);
    }
  }, 10000);
  console.log('ending');
  return "interesting";
}
caller2(myDoubleConsoleLog);
caller2(myDoubleConsoleLog);
