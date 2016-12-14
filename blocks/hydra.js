/**
 * @license
 * Visual Blocks Editor
 *
 * Copyright 2012 Google Inc.
 * https://developers.google.com/blockly/
 *
 * Licensed under the Apache License, Version 2.0 (the "License");
 * you may not use this file except in compliance with the License.
 * You may obtain a copy of the License at
 *
 *   http://www.apache.org/licenses/LICENSE-2.0
 *
 * Unless required by applicable law or agreed to in writing, software
 * distributed under the License is distributed on an "AS IS" BASIS,
 * WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
 * See the License for the specific language governing permissions and
 * limitations under the License.
 */

/**
 * @fileoverview Text blocks for Blockly.
 * @author fraser@google.com (Neil Fraser)
 */
'use strict';

goog.require('Blockly.Blocks');


Blockly.Blocks['motor_control'] = {
  init: function() {
    this.appendDummyInput()
        .appendField("Motor");
    this.appendDummyInput()
        .appendField("Side")
        .appendField(new Blockly.FieldDropdown([["Left", "leftSide"], ["Right", "rightSide"], ["Both", "bothSides"]]), "side");
    this.appendDummyInput()
        .appendField("Speed")
        .appendField(new Blockly.FieldNumber(0, -100, 100), "speed");
    this.setPreviousStatement(true, null);
    this.setNextStatement(true, null);
    this.setColour(20);
    this.setTooltip('');
    this.setHelpUrl('http://www.example.com/');
  }
};