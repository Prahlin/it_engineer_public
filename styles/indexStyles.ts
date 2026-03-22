import { StyleSheet } from "react-native";

const styles = StyleSheet.create({
  safeArea: {
    flex: 1,
    backgroundColor: "#0F0F1A",
  },
  container: {
    flex: 1,
    alignItems: "center",
    justifyContent: "center",
    paddingHorizontal: 32,
  },
  logo: {
    width: 96,
    height: 96,
    borderRadius: 24,
    marginBottom: 16,
  },
  title: {
    fontSize: 28,
    fontWeight: "700",
    color: "#FFFFFF",
    marginBottom: 4,
    textAlign: "center",
  },
  subtitle: {
    fontSize: 14,
    color: "#9CA3AF",
    marginBottom: 32,
    textAlign: "center",
  },
  input: {
    width: "100%",
    height: 52,
    backgroundColor: "#1E1E2E",
    borderRadius: 12,
    paddingHorizontal: 16,
    fontSize: 16,
    color: "#FFFFFF",
    borderWidth: 1,
    borderColor: "#2E2E3E",
    marginBottom: 16,
  },
  rememberRow: {
    width: "100%",
    flexDirection: "row",
    alignItems: "center",
    justifyContent: "space-between",
    marginBottom: 24,
  },
  rememberLabel: {
    fontSize: 14,
    color: "#9CA3AF",
  },
  loginButton: {
    width: "100%",
    height: 52,
    backgroundColor: "#4A90D9",
    borderRadius: 12,
    alignItems: "center",
    justifyContent: "center",
  },
  loginButtonText: {
    fontSize: 16,
    fontWeight: "600",
    color: "#FFFFFF",
  },
});

export default styles;
