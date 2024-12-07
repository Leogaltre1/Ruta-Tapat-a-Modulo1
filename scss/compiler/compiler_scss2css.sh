#!/bin/bash
# Receive Directory data SCSS to CSS
echo 'Compilando sass "../emblematic.scss" "../../emblematic.css"'
sass "../emblematic.scss" "../../emblematic.css"
echo 'Compilando sass "../style.scss" "../../style.css"'
sass "../style.scss" "../../style.css"
