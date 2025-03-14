import { type RouteConfig, index, route } from "@react-router/dev/routes";


export default [
  index("routes/home.tsx"),
  route("identifying", "routes/identifying.tsx"),
] satisfies RouteConfig;
