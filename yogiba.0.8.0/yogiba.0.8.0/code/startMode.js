module.exports.function = function startMode(modeinfo) {
  var result = '';
  var result2 = 66;
  var color = modeinfo.color;
  // 선택한 모드에 따라 모드명을 정하여 넘김
  if (modeinfo.mode.color == true) {
    result = '색맹';
  }
  else if (modeinfo.mode.sight == true) {
    result = '시력';

  }
  else if (modeinfo.mode.astigm == true) {
    result = '난시';
  }
  else {
    result = '오류';
  } 
  return result;
}


