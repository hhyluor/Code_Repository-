# Ajax 综合练习

**学习目标**

* 能够结合所学知识,通过Ajax请求天气数据接口,实现天气页面的动态刷新

---

1. 数据接口
`
http://www.tianqiapi.com/api/
`

2. 请求数据格式效果
![接口格式](/jquery/imgs/json.png)

3. 关键字说明
```
	"cityid": 城市ID
	"update_time": 更新时间
	"city": 城市名
	"cityEn": 城市英文名
    "wea": 天气
    "air_level": 空气级别
    "air_tips": 提示
    "tem1": 最高气温
    "tem2": 最低气温
    "win_speed": 风力
```

4. 页面效果
![页面效果](/jquery/imgs/wea.png)

5. HTML 页面代码
```html
    <!-- 实现页面元素布局 -->
    <h3>天气查询</h3>
    <input type="text" name="city" id="city-in">
    <input type="button" onclick="queryWeather()" value="查询">
    <hr>
    <h3>查询结果</h3>
    <ul>
        <li>所在城市: <span id="city">无</span> </li>
        <li>城市天气: <span id="wea">无</span></li>
        <li>城市温度: <span id="tem">无</span></li>
        <li>空气级别: <span id="airlev">无</span></li>
        <li>风力级别: <span id="wins">无</span></li>
        <li>出行提示: <span id="tips">无</span></li>
    </ul>
```

6. Ajax 代码
```javascript
    <script src="js/jquery-1.12.4.min.js"></script>

    <script>
        // 接收数据,为页面更新内容
        function setPageData(city,wea,tem,airlev,wins,tips){
            $('#city').text(city);
            $('#wea').text(wea);
            $('#tem').text(tem);
            $('#airlev').text(airlev);
            $('#wins').text(wins);
            $('#tips').text(tips);
        }
        // 按钮的响应函数,用来发送ajax请求,获取天气信息
        function queryWeather(){
            // 获取输入框中输入的城市名
            var city = $('#city-in').val();
            // 向接口 http://www.tianqiapi.com/api/ 发送 ajax 请求
            // 请求参数为输入框中的城市信息,
            $.get('http://www.tianqiapi.com/api/',{'city': city},function(response){
                // 通过返回的解析后的json数据,提取页面需要的数据
                var city = response.city;
                var wea = response.data[0].wea;
                var tem = response.data[0].tem2 + ' ~ ' + response.data[0].tem1;
                var airlev = response.data[0].air_level;
                var wins = response.data[0].win_speed;
                var tips = response.data[0].air_tips; 
                // 调用函数为页面添加数据
                setPageData(city, wea, tem, airlev, wins, tips);
            },'json').error(function(){
                // 如果请求失败,页面显示无信息
                setPageData('无', '无', '无', '无', '无', '无');
            });
        }
    </script>
```