import { Plus, Trash2 } from "lucide-react";
import { useEffect, useState } from "react";
import { Form } from "react-router";
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
import { Input } from "~/components/ui/input";

interface Face {
  id: string;
  title: string;
}

export default function Identifying() {
  const [faces, setFaces] = useState<Face[]>([]);

  useEffect(() => {
    const storedFaces = localStorage.getItem("faces");
    if (storedFaces) {
      setFaces(JSON.parse(storedFaces));
    }
  }, []);

  useEffect(() => {
    if (faces.length) {
      localStorage.setItem("faces", JSON.stringify(faces));
    }
  }, [faces]);

  const addFaceEntry = () => {
    setFaces((prev) => [
      ...prev,
      {
        id: crypto.randomUUID(),
        title: "",
      },
    ]);
  };

  const updateFaceTitle = (facesId: string, newTitle: string) => {
    setFaces((prev) =>
      prev.map((face) =>
        face.id === facesId ? { ...face, title: newTitle } : face
      )
    );
  };

   const deleteFaces = (id: string) => {
     setFaces((prev) => prev.filter((face) => face.id !== id));
   };


  return (
    <Form
      method="post"
      encType="multipart/form-data"
      action="/identifying/upload"
    >
      <div className="flex justify-items-start items-start gap-4 p-3 min-h-svh">
        {faces.map((face) => (
          <Card key={face.id}>
            <CardHeader>
              <CardTitle>Select a Face to Add to the Dataset</CardTitle>
            </CardHeader>
            <CardContent className="flex flex-col gap-y-4">
              <div>
                <CardDescription>Give the name of the person.</CardDescription>
                <Input
                  type="text"
                  value={face.title}
                  onChange={(e) => updateFaceTitle(face.id, e.target.value)}
                />
              </div>
              <div>
                <CardDescription>
                  Upload an image to enrich your dataset.
                </CardDescription>
                <InputFile name="" />
              </div>
            </CardContent>
            <CardFooter className="flex justify-between">
              <Button>Submit</Button>
              <Button onClick={() => deleteFaces(face.id)}>
                <Trash2 />
              </Button>
            </CardFooter>
          </Card>
        ))}
        <Button type="button" onClick={addFaceEntry}>
          <Plus />
          Add another person
        </Button>
      </div>
    </Form>
  );
}
