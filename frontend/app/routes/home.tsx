import type { Route } from "./+types/home";

export function meta({}: Route.MetaArgs) {
  return [
    { title: "Find people in a photo" },
    {
      name: "main page",
      content: "welcome on IdentiFace to detect know faces in a photo",
    },
  ];
}

export default function Home() {
  return (
    <div className="flex flex-col justify-center items-center min-h-svh">
      <p>Welcome to Identiface</p>
    </div>
  );
}
