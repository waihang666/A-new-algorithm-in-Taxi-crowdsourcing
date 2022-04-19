//api地址修改
const HOST_URL = '//127.0.0.1:5000';
const API_PATH = '//api/crowdsourcinglogistics/getpoi_by_longlat';






$(function (){
    $.ajaxSetup({dataType: 'json'})

    window.map = new BMap.Map("container");
    map.centerAndZoom("北京", 12);// 初始化地图,设置城市和地图级别。
    map.enableScrollWheelZoom(true);//开启鼠标滚轮缩放
    map.addControl(new BMap.ScaleControl());// 添加比例尺控件
    //map.addControl(new BMap.ZoomControl());// 添加缩放控件

    initSearch();
    initCilck();
});



function API(pp) {
    $('#load').show();
    $('#container').hide();
    map.centerAndZoom(pp, 18)
    $.post(HOST_URL + API_PATH, {longtitude: pp.lng, latitude: pp.lat}, function (res) {
        if (res.error_code == 0) {
            var pointSet = [];
            map.clearOverlays();
            for (let k in res.data) {
                var point = new BMap.Point(res.data[k].longitude, res.data[k].latitude);
                pointSet[k] = (new BMap.Marker(point));
                map.addOverlay(pointSet[k]);

                //显示信息
                /*pointSet[k].name=res.data[k].name;
                pointSet[k].addEventListener("click",function (e){
                    var opts = {
                        width: 200,
                        height: 100,
                        title: this.name,
                    };
                    var infoWindow = new BMap.InfoWindow('', opts);
                    map.openInfoWindow(infoWindow, e.point);
                });*/
            }
        }
        $('#load').hide();
        $('#container').show();
    });
}

function initCilck(){
    map.addEventListener('click', function (e) {
        API(e.point);
    });
}



function initSearch() {
    var ac = new BMap.Autocomplete(    //建立一个自动完成的对象
        {
            "input": "suggestId"
            , "location": map
        });

    ac.addEventListener("onhighlight", function (e) {  //鼠标放在下拉列表上的事件
        var str = "";
        var _value = e.fromitem.value;
        var value = "";
        if (e.fromitem.index > -1) {
            value = _value.province + _value.city + _value.district + _value.street + _value.business;
        }
        str = "FromItem<br />index = " + e.fromitem.index + "<br />value = " + value;

        value = "";
        if (e.toitem.index > -1) {
            _value = e.toitem.value;
            value = _value.province + _value.city + _value.district + _value.street + _value.business;
        }
        str += "<br />ToItem<br />index = " + e.toitem.index + "<br />value = " + value;
        document.getElementById("searchResultPanel").innerHTML = str;
    });

    ac.addEventListener("onconfirm", function (e) {    //鼠标点击下拉列表后的事件
        var _value = e.item.value;
        var myValue = _value.province + _value.city + _value.district + _value.street + _value.business;
        document.getElementById("searchResultPanel").innerHTML = "onconfirm<br />index = " + e.item.index + "<br />myValue = " + myValue;

        var local = new BMap.LocalSearch(map, { //智能搜索
            onSearchComplete: function () {
                var pp = local.getResults().getPoi(0).point;    //获取第一个智能搜索的结果
                API(pp);
            }
        });
        local.search(myValue);
    });
}
