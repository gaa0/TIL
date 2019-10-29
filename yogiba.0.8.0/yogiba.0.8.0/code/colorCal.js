module.exports.function = function colorCal(testStart, colorInput, goTest, coinCompare) {
  const console = require('console');
  var blindnessSet = require('blindnessSet.js')

  var cnt = 100;
  var visited = [1, 0, 0, 0, 0, 0, 0, 0, 0, 0]
  var modenum = 0;
  var accept = 0;
  if (coinCompare != undefined){
    modenum = coinCompare;
    if (coinCompare == "크다"){
      modenum = 63;
    }
    else if (coinCompare == "작다"){
      modenum = 63;
    }
    else if (coinCompare == "같다"){
      modenum = 69;
    }
  }
  if (colorInput != undefined) {
    accept = colorInput;
  }
  if (testStart != undefined) {
    if (testStart.colorArray != undefined) {
      cnt = testStart.colorArray.colorStat;

      if (cnt == 100 && coinCompare != undefined) {
        cnt += 900;
      }
      else if(cnt >= 101 && goTest != undefined){
        if ( goTest == '완료' || goTest == '준비' || goTest == '준비완료' || goTest == '준비 완료')
        cnt = 0;
      }
      console.log(cnt);

      if (testStart.colorArray.colorOne != 0) {
        visited[1] = testStart.colorArray.colorOne;
        if (testStart.colorArray.colorOne == -1) {
          visited[1] = colorInput;
        }
      }
      if (testStart.colorArray.colorTwo != 0) {
        visited[2] = testStart.colorArray.colorTwo;
        if (testStart.colorArray.colorTwo == -1) {
          visited[2] = colorInput;
        }
      }
      if (testStart.colorArray.colorThree != 0) {
        visited[3] = testStart.colorArray.colorThree;
        if (testStart.colorArray.colorThree == -1) {
          visited[3] = colorInput;
        }
      }
      if (testStart.colorArray.colorFour != 0) {
        visited[4] = testStart.colorArray.colorFour;
        if (testStart.colorArray.colorFour == -1) {
          visited[4] = colorInput;
        }
      }
      if (testStart.colorArray.colorFive != 0) {
        visited[5] = testStart.colorArray.colorFive;
        if (testStart.colorArray.colorFive == -1) {
          visited[5] = colorInput;
        }
      }
      if (testStart.colorArray.colorSix != 0) {
        visited[6] = testStart.colorArray.colorSix;
        if (testStart.colorArray.colorSix == -1) {
          visited[6] = colorInput;
        }
      }
      if (testStart.colorArray.colorSeven != 0) {
        visited[7] = testStart.colorArray.colorSeven;
        if (testStart.colorArray.colorSeven == -1) {
          visited[7] = colorInput;
        }
      }
      if (testStart.colorArray.colorEight != 0) {
        visited[8] = testStart.colorArray.colorEight;
        if (testStart.colorArray.colorEight == -1) {
          visited[8] = colorInput;
        }
      }
      if (testStart.colorArray.colorNine != 0) {
        visited[9] = testStart.colorArray.colorNine;
        if (testStart.colorArray.colorNine == -1) {
          visited[9] = colorInput;
        }
      }
    }
  }
  var acblind = 0;
  var acweak = 0;
  var normal = 0;
  var rgblind = 0;
  var rgweak = 0;
  var i = 0;
  var buf = 0;
  if (testStart != undefined) {
    if (testStart.colorArray.sightValue > 0) {
      normal = testStart.colorArray.normals
    }
  }
  if (cnt == 9) {
    for (i = 1; i < 10; i++) {
      buf = 0;
      var items = blindnessSet[i - 1];
      if (visited[i] == items.normal) {
        normal += 1;
        buf += 1;
      }
      if (visited[i] == items.rg_color_blindness) {
        rgblind += 1;
        buf += 1;
      }
      if (visited[i] == items.rg_color_weakness) {
        rgweak += 1;
        buf += 1;
      }
      if (visited[i] == items.al_color_blindness) {
        acblind += 1;
        buf += 1;
      }
      if (visited[i] == items.al_color_weakness) {
        acweak += 1;
        buf += 1;
      }
      if (buf == 0) {
        if (items.rg_color_blindness == 0) {
          rgblind += 1;
        }
        if (items.rg_color_weakness == 0) {
          rgweak += 1;
        }
        if (items.al_color_blindness == 0) {
          acblind += 1;
        }
        if (items.al_color_weakness == 0) {
          acweak += 1;
        }
      }
    }
  }

  var svalue = 0;
  var scol = 0;
  var sscore = 0;
  if (testStart != undefined) {
    sightsize = [40, 1, 2, 4, 6, 8, 10, 12, 15, 20];
    svalue = testStart.colorArray.sightValue;
    scol = testStart.colorArray.sightCorrect;
    sscore = sightsize.indexOf(testStart.colorArray.sightScore);
  }
  if (testStart != undefined) {
    if (testStart.colorArray.normals >= 100) {
      normal = testStart.colorArray.normals;
    }
  }
  if (testStart != undefined) {
    if (goTest != undefined && testStart.colorArray.sightValue == 0) {
      
      accept = testStart.colorArray.colorAccept;
      if (goTest == '네' || goTest == '예' || goTest == '네네' ) {
        acblind += 1;
        if (normal < 400) {
          accept += 1;
        }
        else {
          accept += 10;
        }
      }
      else if (goTest == '아니오' || goTest == '아니요' || goTest == '아니') {
        acblind += 1;
      }
    }
  }
  
  if (testStart != undefined) {
    if(scol == 200){
      if (goTest == '준비' || goTest == '완료' || goTest == '준비완료' || goTest == '준비 완료'){
      acweak = 1;
      }
    }

    if(normal == 100 || normal == 400){
      if (goTest == '준비' || goTest == '완료' || goTest == '준비완료' || goTest == '준비 완료'){
        acweak = 1;
      }
    }
  }

  return {
    colorOne: visited[1],
    colorTwo: visited[2],
    colorThree: visited[3],
    colorFour: visited[4],
    colorFive: visited[5],
    colorSix: visited[6],
    colorSeven: visited[7],
    colorEight: visited[8],
    colorNine: visited[9],
    colorStat: cnt,
    modeNum: modenum, 
    aCBlind: acblind,
    aCWeak: acweak,
    normals: normal,
    rGBlind: rgblind,
    rGWeak: rgweak,
    colorAccept: accept,
    sightValue: svalue,
    sightCorrect: scol,
    sightScore: sscore,
  }
}
