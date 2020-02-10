#!/usr/bin/node
exports.converter = function (base) {
  return function (num) {
    let result = '';
    while (num > base) {
      const remainder = num % base;
      if (remainder >= 10) {
        result += String.fromCharCode(97 + (remainder - 10));
      } else {
        result = remainder + result;
      }
      num = num / base;
    }
    if (num >= 10) {
      return String.fromCharCode(97 + (num - 10)) + result;
    }
    result = Math.floor(num) + result;
    return result;
  };
};
