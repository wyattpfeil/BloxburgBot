var robot = require("robotjs");

var positionToMoveToX = process.argv[2]
var positionToMoveToY = process.argv[3]

robot.moveMouseSmooth(positionToMoveToX, positionToMoveToY);