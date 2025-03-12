import InputFile from "~/components/InputFiles/input-files";
import { Button } from "~/components/ui/button";
import {
  Card,
  CardContent,
  CardDescription,
  CardFooter,
  CardHeader,
  CardTitle,
} from "~/components/ui/card";

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

export default function Identifying() {
  return (
    <div className="flex flex-col justify-center items-center min-h-svh">
      <Card>
        <CardHeader>
          <CardTitle>Select a Face to Add to the Dataset</CardTitle>
          <CardDescription>
            Upload an image to enrich your dataset.
          </CardDescription>
        </CardHeader>
        <CardContent>
          <InputFile />
        </CardContent>
        <CardFooter className="flex justify-between">
          <Button>Submit</Button>
        </CardFooter>
      </Card>
    </div>
  );
}
