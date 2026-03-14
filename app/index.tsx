import { router } from "expo-router";
import { useCallback, useState } from "react";
import {
  Image,
  Switch,
  Text,
  TextInput,
  TouchableOpacity,
  View,
} from "react-native";
import { SafeAreaView } from "react-native-safe-area-context";
import TwirlBackground from "../components/TwirlBackground";
import styles from "../styles/indexStyles";

export default function Index() {
  const [remember, setRemember] = useState(false);

  // Stable callback reference — avoids recreating the function on every render.
  const handleLogin = useCallback(() => router.push("/home"), []);

  return (
    <SafeAreaView style={styles.safeArea}>
      <TwirlBackground />
      <View style={styles.container}>
        <Image
          source={require("../assets/logo.png")}
          style={styles.logo}
          resizeMode="contain"
        />
        <Text style={styles.title}>Welcome Back</Text>
        <Text style={styles.subtitle}>Sign in to continue</Text>
        <TextInput
          style={styles.input}
          placeholder="Email"
          placeholderTextColor="#6B7280"
          keyboardType="email-address"
          autoCapitalize="none"
        />
        <TextInput
          style={styles.input}
          placeholder="Password"
          placeholderTextColor="#6B7280"
          secureTextEntry
        />
        <View style={styles.rememberRow}>
          <Text style={styles.rememberLabel}>Remember Me</Text>
          <Switch
            value={remember}
            onValueChange={setRemember}
            trackColor={{ false: "#2E2E3E", true: "#4A90D9" }}
            thumbColor={remember ? "#FFFFFF" : "#6B7280"}
          />
        </View>
        <TouchableOpacity
          style={styles.loginButton}
          onPress={handleLogin}
          activeOpacity={0.85}
        >
          <Text style={styles.loginButtonText}>Log In</Text>
        </TouchableOpacity>
      </View>
    </SafeAreaView>
  );
}
