#pragma once

/*
 * RAMPS 1.4 <-> NUCLEO-F767ZI adapter pin map
 * Zio-only design: CN7/CN8/CN9/CN10, no Morpho.
 * Logical names below refer to STM32 GPIOs used by firmware.
 */

/* Stepper control */
#define X_STEP_PORT GPIOA
#define X_STEP_PIN  GPIO_PIN_0
#define X_DIR_PORT  GPIOD
#define X_DIR_PIN   GPIO_PIN_13
#define X_EN_PORT   GPIOD
#define X_EN_PIN    GPIO_PIN_12

#define Y_STEP_PORT GPIOB
#define Y_STEP_PIN  GPIO_PIN_0
#define Y_DIR_PORT  GPIOD
#define Y_DIR_PIN   GPIO_PIN_11
#define Y_EN_PORT   GPIOE
#define Y_EN_PIN    GPIO_PIN_2

#define Z_STEP_PORT GPIOB
#define Z_STEP_PIN  GPIO_PIN_10
#define Z_DIR_PORT  GPIOE
#define Z_DIR_PIN   GPIO_PIN_0
#define Z_EN_PORT   GPIOE
#define Z_EN_PIN    GPIO_PIN_15

#define E0_STEP_PORT GPIOB
#define E0_STEP_PIN  GPIO_PIN_11
#define E0_DIR_PORT  GPIOE
#define E0_DIR_PIN   GPIO_PIN_14
#define E0_EN_PORT   GPIOE
#define E0_EN_PIN    GPIO_PIN_12

#define E1_STEP_PORT GPIOE
#define E1_STEP_PIN  GPIO_PIN_10
#define E1_DIR_PORT  GPIOE
#define E1_DIR_PIN   GPIO_PIN_7
#define E1_EN_PORT   GPIOE
#define E1_EN_PIN    GPIO_PIN_8

/* Endstops */
#define X_MIN_PORT GPIOC
#define X_MIN_PIN  GPIO_PIN_8
#define X_MAX_PORT GPIOC
#define X_MAX_PIN  GPIO_PIN_9
#define Y_MIN_PORT GPIOC
#define Y_MIN_PIN  GPIO_PIN_10
#define Y_MAX_PORT GPIOC
#define Y_MAX_PIN  GPIO_PIN_11
#define Z_MIN_PORT GPIOC
#define Z_MIN_PIN  GPIO_PIN_12
#define Z_MAX_PORT GPIOD
#define Z_MAX_PIN  GPIO_PIN_2

/* Power outputs */
#define HOTEND_PWM_PORT GPIOD
#define HOTEND_PWM_PIN  GPIO_PIN_14
#define FAN_PWM_PORT    GPIOD
#define FAN_PWM_PIN     GPIO_PIN_15
#define BED_PWM_PORT    GPIOE
#define BED_PWM_PIN     GPIO_PIN_9

/* ADC */
#define TEMP0_ADC_PORT GPIOA
#define TEMP0_ADC_PIN  GPIO_PIN_3
#define TEMP1_ADC_PORT GPIOC
#define TEMP1_ADC_PIN  GPIO_PIN_0
#define TEMPBED_ADC_PORT GPIOC
#define TEMPBED_ADC_PIN  GPIO_PIN_3

/* Hardware timer recommendations */
#define X_STEP_TIMER      TIM2
#define Y_STEP_TIMER      TIM3
#define Z_STEP_TIMER      TIM2
#define E0_STEP_TIMER     TIM2
#define E1_STEP_TIMER     TIM1
#define HOTEND_PWM_TIMER  TIM4
#define FAN_PWM_TIMER     TIM4
#define BED_PWM_TIMER     TIM1

/* Notes:
 * - Adapter translates STEP/DIR/ENABLE and D8/D9/D10 to RAMPS 5 V logic using 74AHCT244.
 * - Endstops are buffered to 3.3 V using 74LVC541A.
 * - Thermistor ADC inputs are attenuated 2/3 in hardware.
 */
