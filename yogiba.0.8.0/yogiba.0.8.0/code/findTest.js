module.exports.function = function findtest(modeName, colorArray) {// 예) (3, 4, plus(더하기))
  const console = require('console');
  var result = 0;
  var name = String(modeName); // 선택한 모드이름을 가져옴
  var cnt = 0;
  var scr = 0;
  var buf = 1;
  var modenum = 66

  if (name == "색맹") { // 모드이름이 색맹이면
    var visited = [1, 0, 0, 0, 0, 0, 0, 0, 0, 0]; // 리스트를 만들어 이미 값을 받은 사진은 스킵
    if (colorArray != undefined) {
      cnt = colorArray.colorStat;
      if (cnt != 101){
      cnt += 1;
      }
      if (colorArray.colorOne > 0) {
        visited[1] = colorArray.colorOne;
      }
      if (colorArray.colorTwo > 0) {
        visited[2] = colorArray.colorTwo;
      }
      if (colorArray.colorThree > 0) {
        visited[3] = colorArray.colorThree;
      }
      if (colorArray.colorFour > 0) {
        visited[4] = colorArray.colorFour;
      }
      if (colorArray.colorFive > 0) {
        visited[5] = colorArray.colorFive;
      }
      if (colorArray.colorSix > 0) {
        visited[6] = colorArray.colorSix;
      }
      if (colorArray.colorSeven > 0) {
        visited[7] = colorArray.colorSeven;
      }
      if (colorArray.colorEight > 0) {
        visited[8] = colorArray.colorEight;
      }
      if (colorArray.colorNine > 0) {
        visited[9] = colorArray.colorNine;
      }
      if(visited[5] != 12 && visited[5] != 0 && visited[5] != -1){
        cnt = 1001;
      }
    }
    if (cnt <= 9) { // 남은 사진중 랜덤으로 출력하기 위한 코드
      result = Math.floor(Math.random() * 9) + 1;
      if (visited[result] != 0) {
        while (visited[result] != 0) {
          result = Math.floor(Math.random() * 9) + 1;
        }
      }
    }
    else { // 모든사진을 돌았을때 결과화면으로 넘어가기 위한 코드
      result = 10;
    }
    visited[result] = -1;
    if (result < 10) { // 검사중 넘길 변수
      return {
        modeName: name,
        colorOutput: result,
        colorArray: {
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
        }
      }
    }
    else { // 검사가 끝난후 넘길 변수
      return {
        modeName: name,
        colorOutput: result,
        colorArray: {
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
          aCBlind: colorArray.aCBlind,
          aCWeak: colorArray.aCWeak,
          normals: colorArray.normals,
          rGBlind: colorArray.rGBlind,
          rGWeak: colorArray.rGWeak,
        }
      }
    }
  }
  else if (name == "시력") {
    visited = [40, 1, 2, 4, 6, 8, 10, 12, 15, 20];
    buf = colorArray.colorStat;
    normals = colorArray.normals;
    modenum = colorArray.modeNum;
    flag = colorArray.aCWeak;
    if (colorArray.sightScore == undefined) {
      cnt = 0;
    }
    if (colorArray.sightCorrect == undefined) {
      scr = 0;
    }
    if (buf == 0) {
      if (colorArray.colorAccept != undefined) {
        scr = colorArray.sightCorrect;
        cnt = colorArray.sightScore;
        console.log(cnt);

        if (scr == -1) {
          scr = 0;
        }
        else if (colorArray.colorAccept == colorArray.sightValue) {
          scr += 1;
          console.log(colorArray.sightCorrect);
          console.log(colorArray.colorAccept);
          console.log(colorArray.sightValue);
        }
        else {
          scr += 10;
        }
      }
    }
    console.log(scr);
    if (scr >= 200) {
      if (scr == 210 && flag){
        scr = 0;
      }
      else{
        scr = 200;
      }
    }
    else if (scr % 10 > 0 && scr > 0 && cnt < 5) {
      cnt += 1;
      scr = 0;
    }
    else if (scr % 10 > 1 && scr > 0) {
      cnt += 1;
      scr = 0;
    }
    else if (Math.floor(scr / 10) > 1) {
      if (normals == 0) {
        normals = visited[cnt];
        cnt = 0;
        scr = 200;
      }
      else {
        scr = 100;

      }
    }
    console.log(cnt);

    if (cnt == 8) {
      if (normals == 0) {
        normals = visited[cnt];
        cnt = 0;
        scr = 200;
      }
      else {
        scr = 100;

      }
    }



    var past_result = result;
    while (result > 10 || result < 2) {
      result = Math.floor(Math.random() * 9) + 1;
      if (past_result == result) {
        result = Math.floor(Math.random() * 9) + 1;
      }
    }
    console.log(cnt);

    if (buf == 100) {
      scr = -1;
    }
    return {
      modeName: name,
      colorArray: {
        sightValue: result,
        sightScore: visited[cnt],
        sightCorrect: scr,
        colorStat: buf,
        normals: normals,
        modeNum: modenum,
        aCWeak: flag,
      },
    }
  }
  else if (name == "난시") {
    buf = colorArray.normals;
    scr = colorArray.colorAccept;
    cnt = colorArray.aCBlind;
    flag = colorArray.aCWeak;
    if ((buf < 800 && cnt == 1) || buf <= 100 || buf == 400) {
      buf += 100;
      cnt = 0;
    }
    if (flag == 0 ){
      if (buf == 200 || buf == 500){
      buf -= 100;
      }
    }
    return {
      colorArray: {
        normals: buf,
        colorAccept: scr,
        sightValue: 0,
        aCBlind: cnt,
        aCWeak: flag,
      },

      modeName: name,
    }
  }
}