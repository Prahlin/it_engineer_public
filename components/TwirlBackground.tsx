import { useEffect, useRef } from "react";
import { Animated, Easing, StyleSheet, View } from "react-native";

export default function TwirlBackground() {
  const rotation = useRef(new Animated.Value(0)).current;

  useEffect(() => {
    Animated.loop(
      Animated.timing(rotation, {
        toValue: 1,
        duration: 20000,
        easing: Easing.linear,
        useNativeDriver: true,
      })
    ).start();
  }, [rotation]);

  const spin = rotation.interpolate({
    inputRange: [0, 1],
    outputRange: ["0deg", "360deg"],
  });

  return (
    <View style={StyleSheet.absoluteFill} pointerEvents="none">
      <Animated.View
        style={[
          styles.circle,
          styles.circleOuter,
          { transform: [{ rotate: spin }] },
        ]}
      />
      <Animated.View
        style={[
          styles.circle,
          styles.circleMiddle,
          {
            transform: [
              {
                rotate: rotation.interpolate({
                  inputRange: [0, 1],
                  outputRange: ["0deg", "-360deg"],
                }),
              },
            ],
          },
        ]}
      />
      <Animated.View
        style={[
          styles.circle,
          styles.circleInner,
          { transform: [{ rotate: spin }] },
        ]}
      />
    </View>
  );
}

const styles = StyleSheet.create({
  circle: {
    position: "absolute",
    borderRadius: 9999,
    borderWidth: 2,
    opacity: 0.15,
  },
  circleOuter: {
    width: 700,
    height: 700,
    top: -200,
    left: -150,
    borderColor: "#4A90D9",
    borderWidth: 40,
  },
  circleMiddle: {
    width: 500,
    height: 500,
    top: -100,
    left: -50,
    borderColor: "#7B4DD9",
    borderWidth: 30,
  },
  circleInner: {
    width: 300,
    height: 300,
    top: 50,
    left: 50,
    borderColor: "#4AD9B8",
    borderWidth: 20,
  },
});
