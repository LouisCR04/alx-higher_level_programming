#!/usr/bin/node
exports.nbOccurences = function (list, searchElement) {
  const occ = list.filter(x => x === searchElement).length;
  return occ;
};
